from pyflink.datastream import StreamExecutionEnvironment, KeyedProcessFunction
from pyflink.datastream.state import MapStateDescriptor, ValueStateDescriptor, StateTtlConfig
from pyflink.common.typeinfo import Types
from pyflink.common.time import Time
from pyflink.datastream.functions import RuntimeContext
from provenance_graph.associated_event import AssociatedEvent
from anomaly_path.anomaly_score_tag_cache import AnomalyScoreTagCache 
from datetime import datetime
from typing import Optional
from anomaly_path.alert_formatter import AlertFormatter
import pickle
import numpy as np
import gensim 
import time
import os
from system_config import alert_path, attack_nodes_dict, topic

class TagBasedAnomalyPathMiningOnFlink(KeyedProcessFunction):
    init_tag_regular_score_threshold = 0.1 

    alert_count = 0
    positive_alert_count = 0
    output_target = "File"

    attack_nodes = attack_nodes_dict[topic]

    def __init__(self):
        self.tags_cache_map = {}
        self.processed_event_count_value = None
        self.mlp_model = None
        self.fasttext = None
        self.attack_nodes_detected = set()
        self.vector_cache = None
        self.start_time = None

    def open(self, runtime_context: RuntimeContext):
        processed_event_count_value_descriptor = ValueStateDescriptor("processed_event_count_value", Types.LONG())
        self.processed_event_count_value = runtime_context.get_state(processed_event_count_value_descriptor)

    # def load_vector(self):
    #     event_vector_path = '/home/yangyangwei/dataset/e3_cadets_preparation_event_2.npy'
    #     self.vector_cache = np.load(event_vector_path, allow_pickle=True)
    #     return None
    
    def process_element(self, associated_event, ctx: 'KeyedProcessFunction.Context'):
        if self.processed_event_count_value.value() is None:
            print('start dectecting...\n')
            self.start_time = time.time()
            self.processed_event_count_value.update(1)

            # Remove the alert file if it exists
            if os.path.exists(alert_path):
                os.remove(alert_path)

            # self.load_vector()
            # Load MLP model 
            with open('/home/yangyangwei/Baseline_Frequency/cadets/data/mlp_model.pkl', 'rb') as file:
                self.mlp_model = pickle.load(file)
        else:
            self.processed_event_count_value.update(self.processed_event_count_value.value() + 1)
        
        # index = associated_event.get_index()
        # name = associated_event.sink_node.get_node_name()
        # if index >= 941979:
        #     print(f"index: {index}")
        #     print(f"processed event count: {self.processed_event_count_value.value()}")
        #     print(f"associated event:{associated_event.preprocess_event()} Regular score: {associated_event.get_regular_score()}")

        if self.processed_event_count_value.value() % 10000 == 0:
            event_count = self.processed_event_count_value.value()
            elapsed_time = time.time() - self.start_time
            processing_speed = event_count / elapsed_time
            print(f"Processed {event_count} events in {elapsed_time:.2f} seconds. \n Speed: {processing_speed:.2f} events/second \n")
            AnomalyScoreTagCache.statistics_alert_info()
        try:
            if self.is_node_tag_cached(associated_event.source_node):
                associated_event.source_node_tag = self.get_tag_cache(associated_event.source_node)
            if self.is_node_tag_cached(associated_event.sink_node):
                associated_event.sink_node_tag = self.get_tag_cache(associated_event.sink_node)

            tag = self.process_event(associated_event)
        except Exception as e:
            return

        if tag is not None:
            alert_json_string = self.alert_generation(tag)
            if self.output_target == "stdout":
                print(alert_json_string)
            elif self.output_target == "File":
                with open(alert_path, "a") as writer:
                    writer.write(alert_json_string)
                    writer.write(self.statistic_of_precision_and_recall() + "\n\n")


    def alert_generation(self, tag):
        self.alert_count += 1

        anomaly_alert_formatter = AlertFormatter(
            tag.get_tag_initialized_time(),
            tag.get_anomaly_score(),
            tag.anomaly_path,
            TagBasedAnomalyPathMiningOnFlink.attack_nodes
        )
        alert_info, attack_nodes = anomaly_alert_formatter.to_json_string()
        self.attack_nodes_detected.update(attack_nodes)
        if attack_nodes:
            self.positive_alert_count += 1
        return alert_info

    def statistic_of_precision_and_recall(self):
        precison = self.positive_alert_count / self.alert_count
        recall = len(self.attack_nodes_detected) / len(TagBasedAnomalyPathMiningOnFlink.attack_nodes)
        return f"Precision: {precison}, Recall: {recall}, TP: {self.positive_alert_count}, FP: {self.alert_count - self.positive_alert_count}, r1: {len(self.attack_nodes_detected)}, r2: {len(TagBasedAnomalyPathMiningOnFlink.attack_nodes)}"

    def set_tag_cache(self, node, tag_cache):
        self.tags_cache_map[node.node_uuid] = tag_cache

    def is_node_tag_cached(self, node):
        return node.node_uuid in self.tags_cache_map

    def get_tag_cache(self, node):
        return self.tags_cache_map.get(node.node_uuid, None)

    def remove_tag_cache(self, node):
        if node.node_uuid in self.tags_cache_map:
            del self.tags_cache_map[node.node_uuid]

    def process_event(self, associated_event):
        self.init_tag(associated_event)
        self.propagate_tag(associated_event)
        self.degrade_tag(associated_event)
        return self.trigger_alert(associated_event)

    def init_tag(self, associated_event) -> None:
        if associated_event.source_node_tag is not None and associated_event.source_node_tag.get_regular_score() <= 1:
            return

        generalized_event = associated_event.copy_generalize()
        event_regular_score = self.get_event_regular_score(generalized_event)
        if event_regular_score <= self.init_tag_regular_score_threshold:
            new_tag = AnomalyScoreTagCache(associated_event, event_regular_score)
            if associated_event.sink_node_tag is None or associated_event.sink_node_tag.should_replace_tag(new_tag):
                self.set_tag_cache(associated_event.sink_node, new_tag)
        else:
            return

    def propagate_tag(self, associated_event) -> None:
        if self.get_tag_cache(associated_event.source_node) is None:
            return
        else:
            generalized_event = associated_event.copy_generalize()
            event_regular_score = self.get_event_regular_score(generalized_event)
            source_tag = self.get_tag_cache(associated_event.source_node)
            
            if source_tag.should_decayed(associated_event):
                self.remove_tag_cache(associated_event.source_node)
                AnomalyScoreTagCache.decayed_tag_count += 1
                return
            
            #avoid the loop in the anomaly path
            if source_tag.avoid_loop(associated_event):
                return

            if source_tag.alert_mark and event_regular_score >= 0.5:
                return
            
            new_tag = source_tag.propagate(associated_event, event_regular_score)
            if associated_event.sink_node_tag is None or associated_event.sink_node_tag.should_replace_tag(new_tag):
                self.set_tag_cache(associated_event.sink_node, new_tag)

    def degrade_tag(self, associated_event) -> None:
        if self.get_tag_cache(associated_event.sink_node) is None:
            return

        sink_tag = self.get_tag_cache(associated_event.sink_node)
        if sink_tag.should_attenuated():
            self.remove_tag_cache(associated_event.sink_node)
            AnomalyScoreTagCache.attenuated_tag_count += 1
        
        # if sink_tag.should_attenuated_path_distance():
        #     self.remove_tag_cache(associated_event.sink_node)
        #     AnomalyScoreTagCache.attenuated_tag_count += 1 
       

    def trigger_alert(self, associated_event) -> Optional[AnomalyScoreTagCache]:
        if self.get_tag_cache(associated_event.sink_node) is None:
            return None

        sink_tag = self.get_tag_cache(associated_event.sink_node)
        if sink_tag.should_trigger_alert():
            if sink_tag.get_alert_mark():
                return None

            if sink_tag.exist_multiple_repeated_entity():
                self.remove_tag_cache(associated_event.sink_node)
                AnomalyScoreTagCache.attenuated_tag_count += 1
                return None
            return sink_tag.trigger_alert()  
        else:
            return None

    def get_event_regular_score(self, associated_event):
        return associated_event.get_regular_score()
    
    def delete_tag_marked_in_anomaly_path(self, tag):
        for event, _ in tag.anomaly_path:
            self.remove_tag_cache(event.sink_node)