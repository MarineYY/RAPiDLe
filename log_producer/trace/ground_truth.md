
## TRACE – Pine Backdoor w/ Drakon Dropper
```json
//146.153.68.151 connect gtcache
{"host_uuid": "E621F964-5A66-0F89-30E0-67ADB2A5EC28", "event_uuid": "7FF4DE96-5639-D663-3C1D-D4B08A2598ED", "event_type": "EVENT_SENDMSG", "event_timestamp": 1523637781561000000, "subject_uuid": "1F52B45B-9618-A060-215D-7BD61ECCAE05", "subject_name": "gtcache", "object_uuid": "A494D8CF-50ED-5620-1FBE-07A0EE363991", "object_path": "146.153.68.151 : 80"}

// gtcache fork gtcache
{"host_uuid": "host_uuid", "event_uuid": "event_uuid", "event_type": "EVENT_FORK", "event_timestamp": "event_timestamp", "subject_uuid": "1F52B45B-9618-A060-215D-7BD61ECCAE05", "subject_name": "gtcache", "object_uuid": "59169A99-4C73-E5E0-1E25-DB232BA80F32", "object_path": "gtcache"}

// gtcache write /tmp/ztmp
{"host_uuid": "E621F964-5A66-0F89-30E0-67ADB2A5EC28", "event_uuid": "0320414A-E82F-97F0-9496-B4259661CFC6", "event_type": "EVENT_WRITE", "event_timestamp": 1523637968165000000, "subject_uuid": "59169A99-4C73-E5E0-1E25-DB232BA80F32", "subject_name": "gtcache", "object_uuid": "93E0C854-95A4-FE1B-245B-6E217A409764", "object_path": "/tmp/ztmp"}

// gtcache modify /tmp/ztmp
{"host_uuid": "E621F964-5A66-0F89-30E0-67ADB2A5EC28", "event_uuid": "A5DA3328-1DB8-EDDD-4637-60CCE0FEFE3E", "event_type": "EVENT_MODIFY_FILE_ATTRIBUTES", "event_timestamp": 1523637968165000000, "subject_uuid": "59169A99-4C73-E5E0-1E25-DB232BA80F32", "subject_name": "gtcache", "object_uuid": "96FE4223-D38F-9D49-C00F-D51954FA7DD4", "object_path": "/tmp/ztmp"}

// /tmp/ztmp load ztmp
{"host_uuid": "E621F964-5A66-0F89-30E0-67ADB2A5EC28", "event_uuid": "E5B14F8B-5D2C-64CD-1175-9149DF73B7A7", "event_type": "EVENT_LOADLIBRARY", "event_timestamp": 1523638066620000000, "subject_uuid": "D64910E4-454E-156D-BF13-BC7AD66F7A6A", "subject_name": "ztmp", "object_uuid": "96FE4223-D38F-9D49-C00F-D51954FA7DD4", "object_path": "/tmp/ztmp"}

//ztmp connect 162.66.239.75
{"host_uuid": "E621F964-5A66-0F89-30E0-67ADB2A5EC28", "event_uuid": "A5BB567A-E73A-4046-640C-ADA374C7E700", "event_type": "EVENT_CONNECT", "event_timestamp": 1523638066620000000, "subject_uuid": "D64910E4-454E-156D-BF13-BC7AD66F7A6A", "subject_name": "ztmp", "object_uuid": "7E6F9A12-EDFA-C87E-B4D5-DB6C782DC6DC", "object_path": "162.66.239.75 : 80"}

//ztmp fork ztmp
{"host_uuid": "E621F964-5A66-0F89-30E0-67ADB2A5EC28", "event_uuid": "39FE061A-5A71-F36D-984B-63CC35149C0F", "event_type": "EVENT_FORK", "event_timestamp": 1523638066624000000, "subject_uuid": "D64910E4-454E-156D-BF13-BC7AD66F7A6A", "subject_name": "ztmp", "object_uuid": "9736A2A7-D8A8-498F-A633-743D7AEAAEDF", "object_path": "ztmp"}

//ztmp exec uname
{"host_uuid": "E621F964-5A66-0F89-30E0-67ADB2A5EC28", "event_uuid": "8FB3F1A5-C1E1-5054-743D-5D7F3964D4B1", "event_type": "EVENT_EXECUTE", "event_timestamp": 1523638066624000000, "subject_uuid": "9736A2A7-D8A8-498F-A633-743D7AEAAEDF", "subject_name": "ztmp", "object_uuid": "66C31C14-7518-0945-62A9-A7BE2735B99A", "object_path": "uname"}
```

