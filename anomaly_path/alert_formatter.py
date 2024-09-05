from typing import List, Tuple

class AlertFormatter:
    def __init__(self, current_time: int, anomaly_score: float, alert_path, attack_nodes):
        self.current_time = current_time
        self.anomaly_score = anomaly_score
        self.alert_path = alert_path
        self.attack_nodes = attack_nodes

    def to_json_string(self) -> str:
        full_alert_json = []
        full_alert_json.append("###############Alert###############\ncurrentTime:" + str(self.current_time) + "\n")
        full_alert_json.append("AnomalyScore: " + str(self.anomaly_score) + "\n")
        full_alert_json.append("AlertPath:\n")
        attack_nodes_detected = set()
        for path in self.alert_path:
            source_uuid = path[0].get_source_uuid()
            sink_uuid = path[0].get_sink_uuid()
            
            if source_uuid in self.attack_nodes:
                attack_nodes_detected.add(source_uuid)

            if sink_uuid in self.attack_nodes:
                attack_nodes_detected.add(sink_uuid)

            # full_alert_json.append(f"{path[0].event_uuid} {path[0]}: {path[1], {path[0].prediction_score}}\n")
            full_alert_json.append(f"{path[0]}: {path[1]}\n")
        
        if len(attack_nodes_detected):
            full_alert_json.append("true positive:\n")
        else:
            full_alert_json.append("false positive:\n")

        return ''.join(full_alert_json), attack_nodes_detected