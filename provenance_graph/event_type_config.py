# class LOG_TYPE:
#         FILE_OP = ['EVENT_OPEN', 'EVENT_READ', 'EVENT_WRITE', 'EVENT_MODIFY_FILE_ATTRIBUTES', 'EVENT_LOADLIBRARY']
#         PROCESS_OP = ['EVENT_FORK', 'EVENT_MODIFY_PROCESS', 'EVENT_EXECUTE']
#         NET_OP = ['EVENT_RECVMSG', 'EVENT_SENDMSG', 'EVENT_CONNECT']

# class EVENT_TYPE:
#         EVENT_OP = ['EVENT_OPEN', 'EVENT_READ', 'EVENT_WRITE', 'EVENT_EXECUTE', 'EVENT_MODIFY_FILE_ATTRIBUTES', 'EVENT_FORK', 'EVENT_MODIFY_PROCESS', 'EVENT_RECVMSG', 'EVENT_SENDMSG', 'EVENT_CONNECT', 'EVENT_LOADLIBRARY']


class LOG_TYPE:
        FILE_OP = ['file read', 'file write', 'file modify', 'process load']
        PROCESS_OP = ['process fork', 'process execute', 'process modify']
        NET_OP = ['network send', 'network receive']

class EVENT_TYPE:
        EVENT_OP = ['file read', 'file write', 'file modify', 'process fork', 'process execute', 'network send', 'network receive', 'process modify', 'process load']
