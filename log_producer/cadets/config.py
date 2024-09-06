event_csv_list = [
    # '/home/dir/dataset/cadets_e3_preparation/e3_cadets_preparation_event_2.csv',
    # '/home/dir/dataset/cadets_e3_preparation/e3_cadets_preparation_event_8.csv',
    '/home/dir/dataset/cadets_e3_preparation/e3_cadets_preparation_event_9.csv'
]

event_npy_list = [
    # '/home/dir/dataset/cadets_e3_preparation/e3_cadets_preparation_event_2.npy',
    # '/home/dir/dataset/cadets_e3_preparation/e3_cadets_preparation_event_8.npy',
    '/home/dir/dataset/cadets_e3_preparation/e3_cadets_preparation_event_9.npy'
]

event_csv_predict_list = [
    # '/home/dir/dataset/cadets_e3_preparation/e3_cadets_preparation_event_2_predict.csv',
    # '/home/dir/dataset/cadets_e3_preparation/e3_cadets_preparation_event_8_predict.csv',
    '/home/dir/dataset/cadets_e3_preparation/e3_cadets_preparation_event_9_predict.csv'
]

log_list = [
    # '/home/dir/dataset/cadets_e3_preparation/e3_cadets_preparation_2.json',
    # '/home/dir/dataset/cadets_e3_preparation/e3_cadets_preparation_8.json',
    '/home/dir/dataset/cadets_e3_preparation/e3_cadets_preparation_9.json'
]

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