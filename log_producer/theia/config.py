json_file_list = [
    "/home/yangyangwei/dataset/theia_e3/ta1-theia-e3-official-1r.json",
    "/home/yangyangwei/dataset/theia_e3/ta1-theia-e3-official-1r.json.1",
    "/home/yangyangwei/dataset/theia_e3/ta1-theia-e3-official-1r.json.2",
    "/home/yangyangwei/dataset/theia_e3/ta1-theia-e3-official-1r.json.3",
    "/home/yangyangwei/dataset/theia_e3/ta1-theia-e3-official-1r.json.4",
    "/home/yangyangwei/dataset/theia_e3/ta1-theia-e3-official-1r.json.5",
    "/home/yangyangwei/dataset/theia_e3/ta1-theia-e3-official-1r.json.6",
    "/home/yangyangwei/dataset/theia_e3/ta1-theia-e3-official-1r.json.7",
    "/home/yangyangwei/dataset/theia_e3/ta1-theia-e3-official-1r.json.8",
    "/home/yangyangwei/dataset/theia_e3/ta1-theia-e3-official-1r.json.9",
    "/home/yangyangwei/dataset/theia_e3/ta1-theia-e3-official-3.json",
    "/home/yangyangwei/dataset/theia_e3/ta1-theia-e3-official-5m.json",
    "/home/yangyangwei/dataset/theia_e3/ta1-theia-e3-official-6r.json",
    "/home/yangyangwei/dataset/theia_e3/ta1-theia-e3-official-6r.json.1",
    "/home/yangyangwei/dataset/theia_e3/ta1-theia-e3-official-6r.json.10",
    "/home/yangyangwei/dataset/theia_e3/ta1-theia-e3-official-6r.json.11",
    "/home/yangyangwei/dataset/theia_e3/ta1-theia-e3-official-6r.json.12",
    "/home/yangyangwei/dataset/theia_e3/ta1-theia-e3-official-6r.json.2",
    "/home/yangyangwei/dataset/theia_e3/ta1-theia-e3-official-6r.json.3",
    "/home/yangyangwei/dataset/theia_e3/ta1-theia-e3-official-6r.json.4",
    "/home/yangyangwei/dataset/theia_e3/ta1-theia-e3-official-6r.json.5",
    "/home/yangyangwei/dataset/theia_e3/ta1-theia-e3-official-6r.json.6",
    "/home/yangyangwei/dataset/theia_e3/ta1-theia-e3-official-6r.json.7",
    "/home/yangyangwei/dataset/theia_e3/ta1-theia-e3-official-6r.json.8",
    "/home/yangyangwei/dataset/theia_e3/ta1-theia-e3-official-6r.json.9"
]

event_csv_list = [
    '/home/yangyangwei/dataset/theia_e3_preparation/e3_theia_preparation_event_23.csv'
]

event_npy_list = [
    '/home/yangyangwei/dataset/theia_e3_preparation/e3_theia_preparation_event_23.npy'
]

event_csv_predict_list = [
    '/home/yangyangwei/dataset/theia_e3_preparation/e3_theia_preparation_event_23_predict.csv'
]

log_list = [
    '/home/yangyangwei/dataset/theia_e3_preparation/e3_theia_preparation_23.json'
]

class LOG_TYPE:
        FILE_OP = ['EVENT_OPEN', 'EVENT_READ', 'EVENT_WRITE', 'EVENT_MODIFY_FILE_ATTRIBUTES', 'EVENT_LOADLIBRARY']
        PROCESS_OP = ['EVENT_FORK', 'EVENT_MODIFY_PROCESS', 'EVENT_EXECUTE']
        NET_OP = ['EVENT_RECV', 'EVENT_SENDMSG', 'EVENT_CONNECT']

class EVENT_TYPE:
        EVENT_OP = ['EVENT_OPEN', 'EVENT_READ', 'EVENT_WRITE', 'EVENT_EXECUTE', 'EVENT_MODIFY_FILE_ATTRIBUTES', 'EVENT_FORK', 'EVENT_MODIFY_PROCESS', 'EVENT_RECVMSG', 'EVENT_SENDMSG', 'EVENT_CONNECT', 'EVENT_LOADLIBRARY']

event_dict = {
        'EVENT_OPEN': 'file write',
        'EVENT_READ': 'file read',
        'EVENT_WRITE': 'file write',
        'EVENT_MODIFY_FILE_ATTRIBUTES': 'file modify',
        'EVENT_EXECUTE': 'process load',
        'EVENT_FORK': 'process fork',
        'EVENT_CONNECT': 'network send',
        'EVENT_MODIFY_PROCESS': 'process modify',
        'EVENT_RECVFROM': 'network receive',
        'EVENT_SENDTO': 'network send'
}