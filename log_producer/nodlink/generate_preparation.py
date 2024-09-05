import json
import os
import sys
import uuid
import re
sys.path.insert(0, '/home/yangyangwei/RAPiDLe')
from log_producer.preparation_log import PreparationLog
from log_producer.nodlink.config import json_file_list, EVENT_TYPE

process_cache = {}
parent_uuid_cache = {}
parent_name_cache = {}

def load_data(path):
    ground_truth = []
    with open(path, 'r') as file:
        for line in file:
            ground_truth.append(line.strip())
    return ground_truth

def parse_network_string(network_string):
    if not network_string or ':' not in network_string:
        return network_string
    network_string = re.sub(r'->', ':', network_string)
    net = network_string.split(':')
    if len(net) == 2:
        return net[0]
    net1 = net[0]
    net2 = net[2]
    return net1 + '->' + net2

def convert_json_to_standard_format(log):
    global socket_count
    host_uuid = log.get('is_warn', 'None')
    
    event_uuid = log['evt.num']
    event_type = log['evt.type']
    event_timestamp = log['evt.time']
    
    standard_format = ''
    if event_type in EVENT_TYPE.FILE_OP:  
        subject_name =  log['proc.name']
        objectPath = parse_network_string(log['fd.name'])
        try:
            subject_uuid = str(uuid.uuid5(uuid.NAMESPACE_DNS, subject_name))
            object_uuid = str(uuid.uuid5(uuid.NAMESPACE_DNS, objectPath))
        except TypeError:
            return None, None
        if event_type not in ('read', 'readv'):
            standard_format = 'Process ' + subject_name + ', relationship, ' + 'File ' + objectPath
        else:
            standard_format = 'File ' + objectPath + ', relationship, ' + 'Process ' + subject_name
        
    elif event_type in EVENT_TYPE.NET_OP:
        subject_name =  log['proc.name']
        objectPath = parse_network_string(log['fd.name'])

        try:
            subject_uuid = str(uuid.uuid5(uuid.NAMESPACE_DNS, subject_name))
            object_uuid = str(uuid.uuid5(uuid.NAMESPACE_DNS, objectPath))
        except TypeError:
            return None, None
        if event_type in ('sendmsg', 'send', 'sendto'):
            standard_format = 'Process ' + subject_name + ', relationship, ' + 'Network Connect ' + objectPath
        else:
            standard_format = 'Network Connect ' + objectPath + ', relationship, ' + 'Process ' + subject_name
    elif event_type in EVENT_TYPE.PROCESS_OP:
        subject_name =  log['proc.pname']
        objectPath = log['proc.name']
        try:
            subject_uuid = str(uuid.uuid5(uuid.NAMESPACE_DNS, subject_name))
            object_uuid = str(uuid.uuid5(uuid.NAMESPACE_DNS, objectPath))
        except TypeError:
            return None, None
        try:
            standard_format = 'Process ' + subject_name + ', relationship, ' + 'Process ' + objectPath
        except TypeError:
            return None, None
    else:
        print(log)
        sys.exit(1)
    
    preparation_log = PreparationLog(host_uuid, event_uuid, event_type, event_timestamp, subject_uuid, subject_name, object_uuid, objectPath)

    return standard_format, preparation_log.to_json()

if __name__ == '__main__':

    for index, file_path in enumerate(json_file_list):
        print('Now processing file is ', file_path)
        if os.path.isfile(file_path): 
            preparation_events = []
            preparation_logs = []
            with open(file_path, 'r') as f:
                for line in f:
                    data = json.loads(line)
                    event_type = data['evt.type']
                    if event_type in EVENT_TYPE.EVENT_OP:
                        standard_data, preparation_log = convert_json_to_standard_format(data)
                        if standard_data is None: continue
                        preparation_events.append(standard_data)
                        preparation_logs.append(preparation_log)


            print('preparation_events: ', len(preparation_events))

            preparation_event_path = f'/home/yangyangwei/dataset/nodlink_preparation/nodlink_preparation_event_{index}.csv'
            preparation_log_path = f'/home/yangyangwei/dataset/nodlink_preparation/nodlink_preparation_{index}.json'
            with open(preparation_event_path, 'w') as f:
                for event in preparation_events:
                    f.write(event + '\n')

            with open(preparation_log_path, 'w') as f:
                for log in preparation_logs:
                    f.write(log + '\n')