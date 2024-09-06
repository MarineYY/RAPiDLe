json_file_list = [
    "/home/dir/dataset/nodlink/benign.json",
    "/home/dir/dataset/nodlink/anomaly.json"
]

event_csv_list = [
    '/home/dir/dataset/nodlink_preparation/nodlink_preparation_event_1.csv'
]

event_npy_list = [
    '/home/dir/dataset/nodlink_preparation/nodlink_preparation_event_1.npy'
]

event_csv_predict_list = [
    '//home/dir/dataset/nodlink_preparation/nodlink_preparation_event_1_predict.csv'
]

log_list = [
    '/home/dir/dataset/nodlink_preparation/nodlink_preparation_1.json'
]

class EVENT_TYPE:
    FILE_OP = ["read", "readv", "write", "writev", "fcntl", "rmdir", "rename", "chmod"]
    PROCESS_OP = ["clone", "pipe", "fork",'execve']
    NET_OP = ["sendmsg", "recvmsg", "recvfrom", "send", "sendto"]
    EVENT_OP = ["read", "readv", "write", "writev", "fcntl", "rmdir", "rename", "chmod", "clone", "pipe", "fork", 'execve', "sendmsg", "recvmsg", "recvfrom", "send", "sendto"]

event_dict = {
    'read': 'file read',
    'readv': 'file read',
    'write': 'file write',
    'writev': 'file write',
    'fcntl': 'file modify',
    'rmdir': 'file modify',
    'rename': 'file modify',
    'chmod': 'file modify',
    'clone': 'process fork',
    'pipe': 'process execute',
    'fork': 'process fork',
    'execve': 'process execute',
    'sendmsg': 'network send',
    'recvmsg': 'network receive',
    'recvfrom': 'network receive',
    'send': 'network send',
    'sendto': 'network send'
}