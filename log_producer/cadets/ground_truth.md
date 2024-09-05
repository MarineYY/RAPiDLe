## 20180406 1100 CADETS – Nginx Backdoor w/ Drakon In-Memory
**start time**: 1523028012096172059 \
**end time**: 1523030692046111295  \
**file**: e3_cadets_preparation_2.json 
```json
// nginx connect 81.49.200.166
{"host_uuid": "83C8ED1F-5045-DBCD-B39F-918F0DF4F851", "event_uuid": "08577256-B00C-5FC8-9A55-3F923FAF03E2", "event_type": "EVENT_RECVFROM", "event_timestamp": 1523028012096172059, "subject_uuid": "674D8313-390A-11E8-BF66-D9AA8AFF4A69", "subject_name": "nginx", "object_uuid": "FFF277E0-39AD-11E8-BF66-D9AA8AFF4A69", "object_path": "81.49.200.166 : 44623"}

// nginx connect 78.205.235.65
{"host_uuid": "83C8ED1F-5045-DBCD-B39F-918F0DF4F851", "event_uuid": "D5AC4D70-9ED5-54B6-9248-9B2D915348F0", "event_type": "EVENT_RECVFROM", "event_timestamp": 1523028012106173690, "subject_uuid": "674D8313-390A-11E8-BF66-D9AA8AFF4A69", "subject_name": "nginx", "object_uuid": "FFF2AE35-39AD-11E8-BF66-D9AA8AFF4A69", "object_path": "78.205.235.65 : 80"}

// nginx connect 200.36.109.214
{"host_uuid": "83C8ED1F-5045-DBCD-B39F-918F0DF4F851", "event_uuid": "FB5A108E-BFFF-5DDC-8C34-6644F849DE78", "event_type": "EVENT_SENDTO", "event_timestamp": 1523028173596169278, "subject_uuid": "674D8313-390A-11E8-BF66-D9AA8AFF4A69", "subject_name": "nginx", "object_uuid": "6034BA72-39AE-11E8-BF66-D9AA8AFF4A69", "object_path": "200.36.109.214 : 80"}

//nginx write vUgefal (open write)
{"host_uuid": "83C8ED1F-5045-DBCD-B39F-918F0DF4F851", "event_uuid": "021FFC85-94A2-5D75-BA3C-A43618A89245", "event_type": "EVENT_WRITE", "event_timestamp": 1523028709886158284, "subject_uuid": "674D8313-390A-11E8-BF66-D9AA8AFF4A69", "subject_name": "nginx", "object_uuid": "F77E454D-CA07-6B5D-87CA-9EFDCD6BA3ED", "object_path": "/tmp/vUgefal"}

//master execute /tmp/vUgefal 
{"host_uuid": "83C8ED1F-5045-DBCD-B39F-918F0DF4F851", "event_uuid": "E3C64B24-4D14-559A-BBB3-34E87DBF25C5", "event_type": "EVENT_EXECUTE", "event_timestamp": 1523028796536154997, "subject_uuid": "D3822AFC-39AF-11E8-BF66-D9AA8AFF4A69", "subject_name": "master", "object_uuid": "F77E454D-CA07-6B5D-87CA-9EFDCD6BA3ED", "object_path": "/tmp/vUgefal"}

//vUgefal write /var/log/devc
{"host_uuid": "83C8ED1F-5045-DBCD-B39F-918F0DF4F851", "event_uuid": "9082692A-9506-5FFC-8FE2-5900CC9F70BA", "event_type": "EVENT_WRITE", "event_timestamp": 1523030692046111295, "subject_uuid": "D3822AFC-39AF-11E8-BF66-D9AA8AFF4A69", "subject_name": "vUgefal", "object_uuid": "4E4F26B0-221A-5950-9A22-3A4F5059636A", "object_path": "/var/log/devc"}

//vUgefal connect 61.167.39.128
{"host_uuid": "83C8ED1F-5045-DBCD-B39F-918F0DF4F851", "event_uuid": "2A366D6B-FAE4-5C90-B724-C83FE4F950AA", "event_type": "EVENT_SENDTO", "event_timestamp": 1523029384976142609, "subject_uuid": "D3822AFC-39AF-11E8-BF66-D9AA8AFF4A69", "subject_name": "vUgefal", "object_uuid": "323ED9A0-39B1-11E8-BF66-D9AA8AFF4A69", "object_path": "61.167.39.128 : 80"}

//vUgefal chmod /var/log/devc
{"datum":{"com.bbn.tc.schema.avro.cdm18.Event":{"uuid":"318602CB-9945-5D02-953F-A97A52F6C15B","sequence":{"long":12904152},"type":"EVENT_MODIFY_FILE_ATTRIBUTES","threadId":{"int":100785},"hostId":"83C8ED1F-5045-DBCD-B39F-918F0DF4F851","subject":{"com.bbn.tc.schema.avro.cdm18.UUID":"D3822AFC-39AF-11E8-BF66-D9AA8AFF4A69"},"predicateObject":{"com.bbn.tc.schema.avro.cdm18.UUID":"4E4F26B0-221A-5950-9A22-3A4F5059636A"},"predicateObjectPath":{"string":"/var/log/devc"},"predicateObject2":null,"predicateObject2Path":null,"timestampNanos":1523030692046111295,"name":{"string":"aue_chmod"},"parameters":{"array":[{"size":-1,"type":"VALUE_TYPE_CONTROL","valueDataType":"VALUE_DATA_TYPE_INT","isNull":false,"name":{"string":"mode"},"runtimeDataType":null,"valueBytes":{"bytes":"01FF"},"provenance":null,"tag":null,"components":null}]},"location":null,"size":null,"programPoint":null,"properties":{"map":{"host":"83c8ed1f-5045-dbcd-b39f-918f0df4f851","return_value":"0","exec":"vUgefal","ppid":"1281"}}}},"CDMVersion":"18","source":"SOURCE_FREEBSD_DTRACE_CADETS"}
```

## 20180411 1500 CADETS – Nginx Backdoor w/ Drakon In-Memory
**start time**: 1523473712359835172 \
**end time**: 1523473953709828247  \
**file**: e3_cadets_preparation_7.json
```json
'2720E25F-39BE-11E8-B8CE-15D78AC88FB6'
'BA00F667-3DBB-11E8-B8CE-15D78AC88FB6'
'BA012C50-3DBB-11E8-B8CE-15D78AC88FB6'
'BA2C1AFC-3DBB-11E8-B8CE-15D78AC88FB6'
'BB708522-73C1-5C54-8173-BA74545C965F'

//nginx connect network
{"host_uuid": "83C8ED1F-5045-DBCD-B39F-918F0DF4F851", "event_uuid": "5A92D8F5-59C2-5140-BBEE-0D69E286379A", "event_type": "EVENT_RECVFROM", "event_timestamp": 1523473712359835172, "subject_uuid": "2720E25F-39BE-11E8-B8CE-15D78AC88FB6", "subject_name": "nginx", "object_uuid": "BA00F667-3DBB-11E8-B8CE-15D78AC88FB6", "object_path": "25.159.96.207 : 36673"}

{"host_uuid": "83C8ED1F-5045-DBCD-B39F-918F0DF4F851", "event_uuid": "7C66D31C-9A84-5869-A135-9C17AEFAA70C", "event_type": "EVENT_CONNECT", "event_timestamp": 1523473712359835172, "subject_uuid": "2720E25F-39BE-11E8-B8CE-15D78AC88FB6", "subject_name": "nginx", "object_uuid": "BA012C50-3DBB-11E8-B8CE-15D78AC88FB6", "object_path": "76.56.184.25 : 80"}

{"host_uuid": "83C8ED1F-5045-DBCD-B39F-918F0DF4F851", "event_uuid": "00DBA7BF-DE3A-53DE-B52F-FAC217D7908F", "event_type": "EVENT_CONNECT", "event_timestamp": 1523473712639832849, "subject_uuid": "2720E25F-39BE-11E8-B8CE-15D78AC88FB6", "subject_name": "nginx", "object_uuid": "BA2C1AFC-3DBB-11E8-B8CE-15D78AC88FB6", "object_path": "155.162.39.48 : 80"}

//nginx open/write grain
{"host_uuid": "83C8ED1F-5045-DBCD-B39F-918F0DF4F851", "event_uuid": "A9630691-9EA4-5829-8494-B0FC974143FD", "event_type": "EVENT_OPEN", "event_timestamp": 1523473953709828247, "subject_uuid": "2720E25F-39BE-11E8-B8CE-15D78AC88FB6", "subject_name": "nginx", "object_uuid": "BB708522-73C1-5C54-8173-BA74545C965F", "object_path": "/tmp/grain"}

//nginx modify_file_attribution grain
```

## 20180412 1400 CADETS – Nginx Backdoor w/ Drakon In-Memory
**start time**: 1523556022876190369 \
**end time**: 1523558131806155232  \
**file**: e3_cadets_preparation_8.json

```json
'11C64B2C-3DC3-11E8-A5CA-3FA3753A265A' nginx
'5EE4F8FC-3E7B-11E8-A5CB-3FA3753A265A' 25.159.96.207
'5EE54774-3E7B-11E8-A5CB-3FA3753A265A' 76.56.184.25
'5F12229C-3E7B-11E8-A5CB-3FA3753A265A' 155.162.39.48
'5026C48F-56BA-3E5B-BA56-DD382B3EC82B' /tmp/XIM
'219DE547-3E7E-11E8-A5CB-3FA3753A265A' XIM
'21A20E29-3E7E-11E8-A5CB-3FA3753A265A' 53.158.101.118
'48289024-3E7E-11E8-A5CB-3FA3753A265A' XIM
'84D440C2-4E50-4A5C-904E-C4772C4ACD5A' /tmp/test
'47E61FFC-3E80-11E8-A5CB-3FA3753A265A' test
'47EA0B5C-3E80-11E8-A5CB-3FA3753A265A' 192.113.144.28
//nginx connect 25.159.96.207
{"host_uuid": "83C8ED1F-5045-DBCD-B39F-918F0DF4F851", "event_uuid": "21944BC3-1FFB-59C4-8B2E-18AC7F2020CE", "event_type": "EVENT_RECVFROM", "event_timestamp": 1523556022876190369, "subject_uuid": "11C64B2C-3DC3-11E8-A5CA-3FA3753A265A", "subject_name": "nginx", "object_uuid": "5EE4F8FC-3E7B-11E8-A5CB-3FA3753A265A", "object_path": "25.159.96.207 : 45203"}
File /etc/passwd, file read, Process nginx
Process nginx, file open, File /etc/passwd
//nginx connect 76.56.184.25
{"host_uuid": "83C8ED1F-5045-DBCD-B39F-918F0DF4F851", "event_uuid": "E1EEC283-AA82-52C9-9677-498A5B9BE13B", "event_type": "EVENT_CONNECT", "event_timestamp": 1523556022876190369, "subject_uuid": "11C64B2C-3DC3-11E8-A5CA-3FA3753A265A", "subject_name": "nginx", "object_uuid": "5EE54774-3E7B-11E8-A5CB-3FA3753A265A", "object_path": "76.56.184.25 : 80"}

//nginx connect 155.162.39.48
{"host_uuid": "83C8ED1F-5045-DBCD-B39F-918F0DF4F851", "event_uuid": "EBFB7595-F532-54F8-B51B-CE074AAAFE37", "event_type": "EVENT_CONNECT", "event_timestamp": 1523556023166196193, "subject_uuid": "11C64B2C-3DC3-11E8-A5CA-3FA3753A265A", "subject_name": "nginx", "object_uuid": "5F12229C-3E7B-11E8-A5CB-3FA3753A265A", "object_path": "155.162.39.48 : 80"}

// //nginx open/write /tmp/tmux-1002
// {"host_uuid": "83C8ED1F-5045-DBCD-B39F-918F0DF4F851", "event_uuid": "998EEA20-F4C0-54F8-B0E8-355F8800EF2E", "event_type": "EVENT_OPEN", "event_timestamp": 1523556130376185722, "subject_uuid": "11C64B2C-3DC3-11E8-A5CA-3FA3753A265A", "subject_name": "nginx", "object_uuid": "5453C813-1A0E-4359-8E1A-41B40943CDC5", "object_path": "/tmp/tmux-1002"}

// //(1) master elevate /tmp/tmux-1002 
// {"host_uuid": "83C8ED1F-5045-DBCD-B39F-918F0DF4F851", "event_uuid": "3A4EE616-BE69-5C68-BB36-C2D9796A6B5B", "event_type": "EVENT_EXECUTE", "event_timestamp": 1523556194106186440, "subject_uuid": "C4F4FF22-3E7B-11E8-A5CB-3FA3753A265A", "subject_name": "master", "object_uuid": "5453C813-1A0E-4359-8E1A-41B40943CDC5", "object_path": "/tmp/tmux-1002"}

// //(2) sshd elevate /tmp/tmux-1002 
// {"host_uuid": "83C8ED1F-5045-DBCD-B39F-918F0DF4F851", "event_uuid": "E458CE74-090D-543A-9DA3-85D1E18F2800", "event_type": "EVENT_EXECUTE", "event_timestamp": 1523556405396185538, "subject_uuid": "42E4A848-3E7C-11E8-A5CB-3FA3753A265A", "subject_name": "sshd", "object_uuid": "5453C813-1A0E-4359-8E1A-41B40943CDC5", "object_path": "/tmp/tmux-1002"}

// //(3) cron elevate /tmp/tmux-1002 (fail, remove)
// {"host_uuid": "83C8ED1F-5045-DBCD-B39F-918F0DF4F851", "event_uuid": "77085146-18FC-50EC-8D26-8B524B4FCD91", "event_type": "EVENT_EXECUTE", "event_timestamp": 1523556600036180575, "subject_uuid": "B6E5EA8F-3E7C-11E8-A5CB-3FA3753A265A", "subject_name": "cron", "object_uuid": "74BBE554-23FD-D455-BD23-D32CC5D43B28", "object_path": "/tmp/tmux-1002"}


// //nginx open/write /tmp/minions
// {"host_uuid": "83C8ED1F-5045-DBCD-B39F-918F0DF4F851", "event_uuid": "64A46D7C-902C-52A8-B76A-8185123C1E2B", "event_type": "EVENT_OPEN", "event_timestamp": 1523556751146174254, "subject_uuid": "11C64B2C-3DC3-11E8-A5CA-3FA3753A265A", "subject_name": "nginx", "object_uuid": "74D78344-4A18-265B-984A-8D22BB26DDCF", "object_path": "/tmp/minions"}

// //(1)master elevate /tmp/minions 
// {"host_uuid": "83C8ED1F-5045-DBCD-B39F-918F0DF4F851", "event_uuid": "C00C73B6-F952-5E57-BF20-80413CBA5A52", "event_type": "EVENT_EXECUTE", "event_timestamp": 1523556762536176905, "subject_uuid": "17C4C0C3-3E7D-11E8-A5CB-3FA3753A265A", "subject_name": "master", "object_uuid": "74D78344-4A18-265B-984A-8D22BB26DDCF", "object_path": "/tmp/minions"}

// //(2)sshd elevate /tmp/minions
// {"host_uuid": "83C8ED1F-5045-DBCD-B39F-918F0DF4F851", "event_uuid": "6FEFAC0C-064F-5EBB-AAD9-AFCE9AAC8FAF", "event_type": "EVENT_EXECUTE", "event_timestamp": 1523556929346168722, "subject_uuid": "7B30E76D-3E7D-11E8-A5CB-3FA3753A265A", "subject_name": "sshd", "object_uuid": "74D78344-4A18-265B-984A-8D22BB26DDCF", "object_path": "/tmp/minions"}

// //nginx open/write /tmp/font
// {"host_uuid": "83C8ED1F-5045-DBCD-B39F-918F0DF4F851", "event_uuid": "472612BA-8A97-51F1-927A-54B3D2EEEA38", "event_type": "EVENT_OPEN", "event_timestamp": 1523557036346166139, "subject_uuid": "11C64B2C-3DC3-11E8-A5CA-3FA3753A265A", "subject_name": "nginx", "object_uuid": "F993C224-C6AD-AB5C-ADC6-09316CABFFD8", "object_path": "/tmp/font"}

// //(1)elevate /tmp/font (fail, remove)
// {"host_uuid": "83C8ED1F-5045-DBCD-B39F-918F0DF4F851", "event_uuid": "310DD1F1-2D2A-5CDC-8726-0D6296384796", "event_type": "EVENT_EXECUTE", "event_timestamp": 1523557044046166780, "subject_uuid": "BF8EF43F-3E7D-11E8-A5CB-3FA3753A265A", "subject_name": "sshd", "object_uuid": "F993C224-C6AD-AB5C-ADC6-09316CABFFD8", "object_path": "/tmp/font"}

//nginx open/write XIM
{"host_uuid": "83C8ED1F-5045-DBCD-B39F-918F0DF4F851", "event_uuid": "5B00B601-5E7F-510E-A55E-08C16B5916B0", "event_type": "EVENT_OPEN", "event_timestamp": 1523557197146165314, "subject_uuid": "11C64B2C-3DC3-11E8-A5CA-3FA3753A265A", "subject_name": "nginx", "object_uuid": "5026C48F-56BA-3E5B-BA56-DD382B3EC82B", "object_path": "/tmp/XIM"}

//(1)inetd elevate /tmp/XIM
{"host_uuid": "83C8ED1F-5045-DBCD-B39F-918F0DF4F851", "event_uuid": "DB442FC9-5CD9-50AB-B742-057A6F9BB231", "event_type": "EVENT_EXECUTE", "event_timestamp": 1523557208576163772, "subject_uuid": "219DE547-3E7E-11E8-A5CB-3FA3753A265A", "subject_name": "inetd", "object_uuid": "5026C48F-56BA-3E5B-BA56-DD382B3EC82B", "object_path": "/tmp/XIM"}

//XIM connect 53.158.101.118
{"host_uuid": "83C8ED1F-5045-DBCD-B39F-918F0DF4F851", "event_uuid": "52C5A760-8B88-57C6-BFFE-350A31A65885", "event_type": "EVENT_CONNECT", "event_timestamp": 1523557208586166333, "subject_uuid": "219DE547-3E7E-11E8-A5CB-3FA3753A265A", "subject_name": "XIM", "object_uuid": "21A20E29-3E7E-11E8-A5CB-3FA3753A265A", "object_path": "53.158.101.118 : 80"}

//(2) sshd elevate XIM
{"host_uuid": "83C8ED1F-5045-DBCD-B39F-918F0DF4F851", "event_uuid": "524924BA-2082-5E97-A5F8-299EF2C44A6A", "event_type": "EVENT_EXECUTE", "event_timestamp": 1523557273216165672, "subject_uuid": "48289024-3E7E-11E8-A5CB-3FA3753A265A", "subject_name": "sshd", "object_uuid": "5026C48F-56BA-3E5B-BA56-DD382B3EC82B", "object_path": "/tmp/XIM"}

//XIM connect 53.158.101.118
{"host_uuid": "83C8ED1F-5045-DBCD-B39F-918F0DF4F851", "event_uuid": "354D448E-ADAE-55E8-81BC-EFE28EC68680", "event_type": "EVENT_CONNECT", "event_timestamp": 1523557273236165054, "subject_uuid": "48289024-3E7E-11E8-A5CB-3FA3753A265A", "subject_name": "XIM", "object_uuid": "482AD2B6-3E7E-11E8-A5CB-3FA3753A265A", "object_path": "53.158.101.118 : 80"}

// //XIM open/write /var/log/netlog
// {"host_uuid": "83C8ED1F-5045-DBCD-B39F-918F0DF4F851", "event_uuid": "7DA691E8-0A31-5FAE-8327-9D4D27EF4F9E", "event_type": "EVENT_OPEN", "event_timestamp": 1523557424536159661, "subject_uuid": "48289024-3E7E-11E8-A5CB-3FA3753A265A", "subject_name": "XIM", "object_uuid": "E5F1BC5B-052D-3F5F-AD05-928A8F3FF746", "object_path": "/var/log/netlog"}

// //(1)cron elevate /var/log/netlog(fail, remove)
// {"host_uuid": "83C8ED1F-5045-DBCD-B39F-918F0DF4F851", "event_uuid": "F6FC91B2-5841-58A9-BB38-330C757A8DFD", "event_type": "EVENT_EXECUTE", "event_timestamp": 1523557500026158747, "subject_uuid": "CF565BC0-3E7E-11E8-A5CB-3FA3753A265A", "subject_name": "cron", "object_uuid": "74BBE554-23FD-D455-BD23-D32CC5D43B28", "object_path": "/var/log/netlog"}

//XIM open/write /var/log/sendmail
// {"host_uuid": "83C8ED1F-5045-DBCD-B39F-918F0DF4F851", "event_uuid": "DECE22D6-7B23-5A78-B42C-2C40C383AF2C", "event_type": "EVENT_OPEN", "event_timestamp": 1523557597066156701, "subject_uuid": "48289024-3E7E-11E8-A5CB-3FA3753A265A", "subject_name": "XIM", "object_uuid": "CBBF8038-5237-8651-B752-A1C99186128A", "object_path": "/var/log/sendmail"}

// //(2)sshd elevate /var/log/sendmail
// {"host_uuid": "83C8ED1F-5045-DBCD-B39F-918F0DF4F851", "event_uuid": "D7974136-9F39-5C89-8D95-F587CCC82C2A", "event_type": "EVENT_EXECUTE", "event_timestamp": 1523557617136153757, "subject_uuid": "15267234-3E7F-11E8-A5CB-3FA3753A265A", "subject_name": "sshd", "object_uuid": "CBBF8038-5237-8651-B752-A1C99186128A", "object_path": "/var/log/sendmail"}

//XIM open/write /tmp/main
// {"host_uuid": "83C8ED1F-5045-DBCD-B39F-918F0DF4F851", "event_uuid": "E0742D22-EF26-5952-B384-60E395D51D37", "event_type": "EVENT_OPEN", "event_timestamp": 1523557727956150660, "subject_uuid": "48289024-3E7E-11E8-A5CB-3FA3753A265A", "subject_name": "XIM", "object_uuid": "4DA445A7-56DB-D353-9B56-AD9CD3D373D6", "object_path": "/tmp/main"}

// //sshd elevate /tmp/main 
// {"host_uuid": "83C8ED1F-5045-DBCD-B39F-918F0DF4F851", "event_uuid": "9A3CA81D-7BD7-5E0C-A5B9-EE6592816B67", "event_type": "EVENT_EXECUTE", "event_timestamp": 1523557737406150415, "subject_uuid": "5CD609A7-3E7F-11E8-A5CB-3FA3753A265A", "subject_name": "sshd", "object_uuid": "4DA445A7-56DB-D353-9B56-AD9CD3D373D6", "object_path": "/tmp/main"}

//XIM open/write /tmp/test
{"host_uuid": "83C8ED1F-5045-DBCD-B39F-918F0DF4F851", "event_uuid": "70318695-9F0F-540F-AF54-00D50000EE45", "event_type": "EVENT_OPEN", "event_timestamp": 1523557941296153503, "subject_uuid": "48289024-3E7E-11E8-A5CB-3FA3753A265A", "subject_name": "XIM", "object_uuid": "84D440C2-4E50-4A5C-904E-C4772C4ACD5A", "object_path": "/tmp/test"}

//XIM elevate /tmp/test
{"host_uuid": "83C8ED1F-5045-DBCD-B39F-918F0DF4F851", "event_uuid": "7FF588AF-3819-5BBC-B53C-3E4872570F05", "event_type": "EVENT_EXECUTE", "event_timestamp": 1523558131776142868, "subject_uuid": "47E61FFC-3E80-11E8-A5CB-3FA3753A265A", "subject_name": "XIM", "object_uuid": "84D440C2-4E50-4A5C-904E-C4772C4ACD5A", "object_path": "/tmp/test"}

//test connect 192.113.144.28
{"host_uuid": "83C8ED1F-5045-DBCD-B39F-918F0DF4F851", "event_uuid": "4030D5CC-A9C0-529F-8466-495BC4B87153", "event_type": "EVENT_CONNECT", "event_timestamp": 1523558131806155232, "subject_uuid": "47E61FFC-3E80-11E8-A5CB-3FA3753A265A", "subject_name": "test", "object_uuid": "47EA0B5C-3E80-11E8-A5CB-3FA3753A265A", "object_path": "192.113.144.28 : 80"}
```

## 20180413 CADETS – Nginx Backdoor w/ Drakon In-Memory
**start time**: 1523624830574650037 \
**end time**: 1523625386684642175  \
**file**: e3_cadets_preparation_9.json
```json
'11C65665-3DC3-11E8-A5CA-3FA3753A265A' nginx
'937BA111-3F1B-11E8-A5CB-3FA3753A265A' 25.159.96.207
'93A2D6AC-3F1B-11E8-A5CB-3FA3753A265A' 155.162.39.48
'E5A15412-68E0-FD54-A068-DD6114FD9040' /tmp/pEja72mA
'0C773AFD-8F2A-3555-AA8F-AFF835357207' /tmp/eWq10bVcx
'4FB0BFEA-3F1C-11E8-A5CB-3FA3753A265A' pEja72mA
'4FB30E44-3F1C-11E8-A5CB-3FA3753A265A' 53.158.101.118
'885AF67E-0E96-FE5D-960E-14BA5DFEBBD3' /tmp/memhelp.so
'6C04A21E-0D75-2B5F-B50D-88F06F2B7BF7' /tmp/eraseme
'2A03F3BA-792D-9C5B-AD79-5A5DEB9CB9D2' done.so
'2CA83801-3E80-11E8-A5CB-3FA3753A265A' sshd
'DEF1F812-3F1C-11E8-A5CB-3FA3753A265A' 198.115.236.119

//nginx connect 25.159.96.207
{"host_uuid": "83C8ED1F-5045-DBCD-B39F-918F0DF4F851", "event_uuid": "810C8CF8-0F83-59CD-B4EF-77F0CD289F71", "event_type": "EVENT_RECVFROM", "event_timestamp": 1523624830574650037, "subject_uuid": "11C65665-3DC3-11E8-A5CA-3FA3753A265A", "subject_name": "nginx", "object_uuid": "937BA111-3F1B-11E8-A5CB-3FA3753A265A", "object_path": "25.159.96.207 : 58625"}

//nginx connect 155.162.39.48
{"host_uuid": "83C8ED1F-5045-DBCD-B39F-918F0DF4F851", "event_uuid": "59984B3F-46B2-5B34-BADF-0A85F939F8E3", "event_type": "EVENT_CONNECT", "event_timestamp": 1523624830834653379, "subject_uuid": "11C65665-3DC3-11E8-A5CA-3FA3753A265A", "subject_name": "nginx", "object_uuid": "93A2D6AC-3F1B-11E8-A5CB-3FA3753A265A", "object_path": "155.162.39.48 : 80"}

//nginx connect 78.205.235.65(fail)

//nginx open/write /tmp/pEja72mA
{"host_uuid": "83C8ED1F-5045-DBCD-B39F-918F0DF4F851", "event_uuid": "EC1E16E2-A3E5-535E-9FC1-7DE6A65A9EFC", "event_type": "EVENT_OPEN", "event_timestamp": 1523625007794656242, "subject_uuid": "11C65665-3DC3-11E8-A5CA-3FA3753A265A", "subject_name": "nginx", "object_uuid": "E5A15412-68E0-FD54-A068-DD6114FD9040", "object_path": "/tmp/pEja72mA"}

//nginx open/write /tmp/eWq10bVcx
{"host_uuid": "83C8ED1F-5045-DBCD-B39F-918F0DF4F851", "event_uuid": "7DBB1800-D1DD-5300-9D44-1A13E9981557", "event_type": "EVENT_OPEN", "event_timestamp": 1523625074974644925, "subject_uuid": "11C65665-3DC3-11E8-A5CA-3FA3753A265A", "subject_name": "nginx", "object_uuid": "0C773AFD-8F2A-3555-AA8F-AFF835357207", "object_path": "/tmp/eWq10bVcx"}

//sshd elevate /tmp/pEja72mA
{"host_uuid": "83C8ED1F-5045-DBCD-B39F-918F0DF4F851", "event_uuid": "B7428FEB-B40E-5794-99F0-0522769F4B55", "event_type": "EVENT_EXECUTE", "event_timestamp": 1523625146344650401, "subject_uuid": "4FB0BFEA-3F1C-11E8-A5CB-3FA3753A265A", "subject_name": "sshd", "object_uuid": "E5A15412-68E0-FD54-A068-DD6114FD9040", "object_path": "/tmp/pEja72mA"}

//pEja72mA connect 53.158.101.118
{"host_uuid": "83C8ED1F-5045-DBCD-B39F-918F0DF4F851", "event_uuid": "ACFA27E0-04BE-59C5-9DE3-18E9D54B8D2B", "event_type": "EVENT_CONNECT", "event_timestamp": 1523625146354648690, "subject_uuid": "4FB0BFEA-3F1C-11E8-A5CB-3FA3753A265A", "subject_name": "pEja72mA", "object_uuid": "4FB30E44-3F1C-11E8-A5CB-3FA3753A265A", "object_path": "53.158.101.118 : 80"}

//pEja72mA read /tmp/eWq10bVcx
{"host_uuid": "83C8ED1F-5045-DBCD-B39F-918F0DF4F851", "event_uuid": "B6316F5A-21F9-53DB-986F-E993F7FF778C", "event_type": "EVENT_OPEN", "event_timestamp": 1523625429714638405, "subject_uuid": "4FB0BFEA-3F1C-11E8-A5CB-3FA3753A265A", "subject_name": "pEja72mA", "object_uuid": "0C773AFD-8F2A-3555-AA8F-AFF835357207", "object_path": "/tmp/eWq10bVcx"}

//pEja72mA write /tmp/memhelp.so
{"host_uuid": "83C8ED1F-5045-DBCD-B39F-918F0DF4F851", "event_uuid": "B7462BF1-A19E-5CEB-9F59-D1C5EB009D04", "event_type": "EVENT_OPEN", "event_timestamp": 1523625429714638405, "subject_uuid": "4FB0BFEA-3F1C-11E8-A5CB-3FA3753A265A", "subject_name": "pEja72mA", "object_uuid": "885AF67E-0E96-FE5D-960E-14BA5DFEBBD3", "object_path": "/tmp/memhelp.so"}

//pEja72mA read /tmp/memhelp.so
{"host_uuid": "83C8ED1F-5045-DBCD-B39F-918F0DF4F851", "event_uuid": "EABB6201-8D0B-52EB-A743-9AE6745E0072", "event_type": "EVENT_OPEN", "event_timestamp": 1523625580714634189, "subject_uuid": "4FB0BFEA-3F1C-11E8-A5CB-3FA3753A265A", "subject_name": "pEja72mA", "object_uuid": "885AF67E-0E96-FE5D-960E-14BA5DFEBBD3", "object_path": "/tmp/memhelp.so"}

//pEja72mA write /tmp/eraseme
{"host_uuid": "83C8ED1F-5045-DBCD-B39F-918F0DF4F851", "event_uuid": "7C04AB0A-E4E5-548C-9A7D-126CC2E5A816", "event_type": "EVENT_OPEN", "event_timestamp": 1523625580714634189, "subject_uuid": "4FB0BFEA-3F1C-11E8-A5CB-3FA3753A265A", "subject_name": "pEja72mA", "object_uuid": "6C04A21E-0D75-2B5F-B50D-88F06F2B7BF7", "object_path": "/tmp/eraseme"}

//pEja72mA read /tmp/eraseme
//pEja72mA write /tmp/done.so
{"host_uuid": "83C8ED1F-5045-DBCD-B39F-918F0DF4F851", "event_uuid": "BF81303C-E1E4-5EB1-A7C3-4C27A149B459", "event_type": "EVENT_WRITE", "event_timestamp": 1523625647144628789, "subject_uuid": "4FB0BFEA-3F1C-11E8-A5CB-3FA3753A265A", "subject_name": "pEja72mA", "object_uuid": "2A03F3BA-792D-9C5B-AD79-5A5DEB9CB9D2", "object_path": "done.so"}

//pEja72mA modify_process pEja72mA
// EVENT_MODIFY_PROCESS, for events that modify the process environment (eg, umask, chdir)
{"host_uuid": "83C8ED1F-5045-DBCD-B39F-918F0DF4F851", "event_uuid": "287F3DFE-C31B-54AC-8387-E978D862BC09", "event_type": "EVENT_MODIFY_PROCESS", "event_timestamp": 1523625189214643072, "subject_uuid": "4FB0BFEA-3F1C-11E8-A5CB-3FA3753A265A", "subject_name": "pEja72mA", "object_uuid": "2CA83801-3E80-11E8-A5CB-3FA3753A265A", "object_path": "sshd"}

//sshd connect 198.115.236.119
{"host_uuid": "83C8ED1F-5045-DBCD-B39F-918F0DF4F851", "event_uuid": "D1C8FEE9-E746-526D-8A73-A46A3FF905BF", "event_type": "EVENT_CONNECT", "event_timestamp": 1523625386684642175, "subject_uuid": "2CA83801-3E80-11E8-A5CB-3FA3753A265A", "subject_name": "sshd", "object_uuid": "DEF1F812-3F1C-11E8-A5CB-3FA3753A265A", "object_path": "198.115.236.119 : 80"}
```

<!-- we need to add new event types, include EVENT_MODIFY_FILE_ATTRIBUTES, EVENT_MODIFY_PROCESS -->

| **Data Type** | **File Name**                    | **Details**    |
|---------------|----------------------------------|----------------|
| Training Data | `e3_cadets_preparation_0.json`   |                |
|               | `e3_cadets_preparation_1.json`   |                |
|               | `e3_cadets_preparation_3.json`   |                |
|               | `e3_cadets_preparation_4.json`   |                |
|               | `e3_cadets_preparation_5.json`   |                |
|               | `e3_cadets_preparation_6.json`   |                |
|               | `e3_cadets_preparation_8.json`   |                |

---

| **Data Type** | **File Name**                    | **Details**    |
|---------------|----------------------------------|----------------|
| Test Data     | `e3_cadets_preparation_2.json`   | One attack     |
|               | `e3_cadets_preparation_7.json`   | Two attacks    |
|               | `e3_cadets_preparation_9.json`   | One attack     |

1.how should we deal with event of inject 


<!-- ```json
associated events with inject 
inject
8603F11E-3F1C-11E8-A5CB-3FA3753A265A sshd 20691

"4FB0BFEA-3F1C-11E8-A5CB-3FA3753A265A" 
"exec":"sshd","ppid":"20691" /tmp/pEja72mA
{"datum":{"com.bbn.tc.schema.avro.cdm18.Event":{"uuid":"287F3DFE-C31B-54AC-8387-E978D862BC09","sequence":{"long":6268627},"type":"EVENT_MODIFY_PROCESS","threadId":{"int":100664},"hostId":"83C8ED1F-5045-DBCD-B39F-918F0DF4F851","subject":{"com.bbn.tc.schema.avro.cdm18.UUID":"4FB0BFEA-3F1C-11E8-A5CB-3FA3753A265A"},"predicateObject":{"com.bbn.tc.schema.avro.cdm18.UUID":"4FB0BFEA-3F1C-11E8-A5CB-3FA3753A265A"},"predicateObjectPath":null,"predicateObject2":{"com.bbn.tc.schema.avro.cdm18.UUID":"3209A26F-A6EF-0350-AFA6-B1BD1003D390"},"predicateObject2Path":{"string":"/tmp"},"timestampNanos":1523625189214643072,"name":{"string":"aue_chdir"},"parameters":{"array":[]},"location":null,"size":null,"programPoint":null,"properties":{"map":{"host":"83c8ed1f-5045-dbcd-b39f-918f0df4f851","return_value":"0","exec":"pEja72mA","ppid":"20691"}}}},"CDMVersion":"18","source":"SOURCE_FREEBSD_DTRACE_CADETS"}

sshd=1 2CA83801-3E80-11E8-A5CB-3FA3753A265A connect 198.115.236.119 1790977
{"datum":{"com.bbn.tc.schema.avro.cdm18.Event":{"uuid":"D1C8FEE9-E746-526D-8A73-A46A3FF905BF","sequence":{"long":6281871},"type":"EVENT_CONNECT","threadId":{"int":100676},"hostId":"83C8ED1F-5045-DBCD-B39F-918F0DF4F851","subject":{"com.bbn.tc.schema.avro.cdm18.UUID":"2CA83801-3E80-11E8-A5CB-3FA3753A265A"},"predicateObject":{"com.bbn.tc.schema.avro.cdm18.UUID":"DEF1F812-3F1C-11E8-A5CB-3FA3753A265A"},"predicateObjectPath":null,"predicateObject2":null,"predicateObject2Path":null,"timestampNanos":1523625386684642175,"name":{"string":"aue_connect"},"parameters":{"array":[]},"location":null,"size":null,"programPoint":null,"properties":{"map":{"return_value":"0","address":"198.115.236.119","port":"80","host":"83c8ed1f-5045-dbcd-b39f-918f0df4f851","fd":"5","exec":"sshd","ppid":"1"}}}},"CDMVersion":"18","source":"SOURCE_FREEBSD_DTRACE_CADETS"}

DEF1F812-3F1C-11E8-A5CB-3FA3753A265A  198.115.236.119 1790976
{"datum":{"com.bbn.tc.schema.avro.cdm18.NetFlowObject":{"uuid":"DEF1F812-3F1C-11E8-A5CB-3FA3753A265A","baseObject":{"hostId":"83C8ED1F-5045-DBCD-B39F-918F0DF4F851","permission":null,"epoch":null,"properties":{"map":{}}},"localAddress":"128.55.12.73","localPort":47282,"remoteAddress":"198.115.236.119","remotePort":80,"ipProtocol":null,"fileDescriptor":null}},"CDMVersion":"18","source":"SOURCE_FREEBSD_DTRACE_CADETS"}

01121F6A-3F1D-11E8-A5CB-3FA3753A265A 198.115.236.119 1800470 sshd pid=1()
{"datum":{"com.bbn.tc.schema.avro.cdm18.NetFlowObject":{"uuid":"01121F6A-3F1D-11E8-A5CB-3FA3753A265A","baseObject":{"hostId":"83C8ED1F-5045-DBCD-B39F-918F0DF4F851","permission":null,"epoch":null,"properties":{"map":{}}},"localAddress":"128.55.12.73","localPort":27885,"remoteAddress":"198.115.236.119","remotePort":80,"ipProtocol":null,"fileDescriptor":null}},"CDMVersion":"18","source":"SOURCE_FREEBSD_DTRACE_CADETS"}
``` -->



















