
## 20180410 1400 THEIA – Firefox Backdoor w/ Drakon In-Memory
e3_theia_preparation_12.json
```json

F71F9730-0000-0000-0000-000000000020 firefox
0100D00F-5EC5-0600-0000-0000697C471C /home/admin/profile
FB1F9E30-0000-0000-0000-000000000020 profile
80370C6E-64B2-A174-5848-500000000040 161.116.88.72

{"host_uuid": "0A00063C-5254-00F0-0D60-000000000070", "event_uuid": "1DC12EDC-0828-2415-DDA1-400000000010", "event_type": "EVENT_OPEN", "event_timestamp": 1523386592476971293, "subject_uuid": "F71F9730-0000-0000-0000-000000000020", "subject_name": "firefox", "object_uuid": "0100D00F-5EC5-0600-0000-0000697C471C", "object_path": "/home/admin/profile"}

{"host_uuid": "0A00063C-5254-00F0-0D60-000000000070", "event_uuid": "ACD92890-0A28-2415-4DB3-400000000010", "event_type": "EVENT_EXECUTE", "event_timestamp": 1523386599791450540, "subject_uuid": "FB1F9E30-0000-0000-0000-000000000020", "subject_name": "profile", "object_uuid": "0100D00F-5EC5-0600-0000-0000697C471C", "object_path": "/home/admin/profile"}

{"host_uuid": "0A00063C-5254-00F0-0D60-000000000070", "event_uuid": "1F0D5990-0A28-2415-63B3-400000000010", "event_type": "EVENT_SENDTO", "event_timestamp": 1523386599794609439, "subject_uuid": "FB1F9E30-0000-0000-0000-000000000020", "subject_name": "profile", "object_uuid": "80370C6E-64B2-A174-5848-500000000040", "object_path": "161.116.88.72 : 80"}


64189C2B-0000-0000-0000-000000000020 firefox
0100D00F-44C5-0600-0000-00006E15B00E /home/admin/clean
6818A92B-0000-0000-0000-000000000020 clean
80370C6E-AAB0-A174-5848-500000000040 161.116.88.72

{"host_uuid": "0A00063C-5254-00F0-0D60-000000000070", "event_uuid": "667FB3F2-DF26-2415-B7F5-3B0000000010", "event_type": "EVENT_OPEN", "event_timestamp": 1523385317249482598, "subject_uuid": "64189C2B-0000-0000-0000-000000000020", "subject_name": "firefox", "object_uuid": "0100D00F-44C5-0600-0000-00006E15B00E", "object_path": "/home/admin/clean"}


{"host_uuid": "0A00063C-5254-00F0-0D60-000000000070", "event_uuid": "D76CBCF4-E226-2415-3BF6-3B0000000010", "event_type": "EVENT_EXECUTE", "event_timestamp": 1523385330168523991, "subject_uuid": "6818A92B-0000-0000-0000-000000000020", "subject_name": "clean", "object_uuid": "0100D00F-44C5-0600-0000-00006E15B00E", "object_path": "/home/admin/clean"}

{"host_uuid": "0A00063C-5254-00F0-0D60-000000000070", "event_uuid": "9795E2F4-E226-2415-4DF6-3B0000000010", "event_type": "EVENT_CONNECT", "event_timestamp": 1523385330171024791, "subject_uuid": "6818A92B-0000-0000-0000-000000000020", "subject_name": "clean", "object_uuid": "80370C6E-AAB0-A174-5848-500000000040", "object_path": "161.116.88.72 : 80"}
```1523386599794609439

## 20180412 THEIA – Browser Extension w/ Drakon Dropper
e3_theia_preparation_23.json
```json
B33501B6-0200-0000-0000-000000000020 firefox
80370C6E-4396-8D2B-B0CB-500000000040 141.43.176.203
0100D00F-B700-2800-0000-00002BDE0334 /etc/firefox/native-messaging-hosts/gtcache
B53501B6-0200-0000-0000-000000000020 dash
80370C6E-39C2-9299-4497-500000000040 146.153.68.151

{"host_uuid": "0A00063C-5254-00F0-0D60-000000000070", "event_uuid": "1F0EFAA0-4EBE-2415-DFF7-620200000010", "event_type": "EVENT_RECVFROM", "event_timestamp": 1523551818875538975, "subject_uuid": "B33501B6-0200-0000-0000-000000000020", "subject_name": "firefox", "object_uuid": "80370C6E-4396-8D2B-B0CB-500000000040", "object_path": "141.43.176.203 : 80"}

{"host_uuid": "0A00063C-5254-00F0-0D60-000000000070", "event_uuid": "FF9BFBA0-4EBE-2415-E1F7-620200000010", "event_type": "EVENT_WRITE", "event_timestamp": 1523551818875640831, "subject_uuid": "B33501B6-0200-0000-0000-000000000020", "subject_name": "firefox", "object_uuid": "0100D00F-B700-2800-0000-00002BDE0334", "object_path": "/etc/firefox/native-messaging-hosts/gtcache"}

{"host_uuid": "0A00063C-5254-00F0-0D60-000000000070", "event_uuid": "26E8DAA1-4EBE-2415-40F8-620200000010", "event_type": "EVENT_EXECUTE", "event_timestamp": 1523551818890274854, "subject_uuid": "B53501B6-0200-0000-0000-000000000020", "subject_name": "dash", "object_uuid": "0100D00F-B700-2800-0000-00002BDE0334", "object_path": "/etc/firefox/native-messaging-hosts/gtcache"}

{"host_uuid": "0A00063C-5254-00F0-0D60-000000000070", "event_uuid": "4ECC6FA4-4EBE-2415-FAF8-620200000010", "event_type": "EVENT_SENDTO", "event_timestamp": 1523551818933587022, "subject_uuid": "B53501B6-0200-0000-0000-000000000020", "subject_name": "dash", "object_uuid": "80370C6E-39C2-9299-4497-500000000040", "object_path": "146.153.68.151 : 80"}

223838BC-0200-0000-0000-000000000020 profile (deleted)
0100D00F-A84B-1E00-0000-00008C1CB31C /var/log/mail
283847BC-0200-0000-0000-000000000020 mail
80370C6E-D2AA-9534-C617-500000000040 149.52.198.23
{"host_uuid": "0A00063C-5254-00F0-0D60-000000000070", "event_uuid": "66B8C7F8-C0BF-2415-3176-670200000010", "event_type": "EVENT_OPEN", "event_timestamp": 1523553409486534758, "subject_uuid": "223838BC-0200-0000-0000-000000000020", "subject_name": "profile (deleted)", "object_uuid": "0100D00F-A84B-1E00-0000-00008C1CB31C", "object_path": "/var/log/mail"}

{"host_uuid": "0A00063C-5254-00F0-0D60-000000000070", "event_uuid": "D3225666-C4BF-2415-2778-670200000010", "event_type": "EVENT_EXECUTE", "event_timestamp": 1523553424209486547, "subject_uuid": "283847BC-0200-0000-0000-000000000020", "subject_name": "mail", "object_uuid": "0100D00F-A84B-1E00-0000-00008C1CB31C", "object_path": "/var/log/mail"}

{"host_uuid": "0A00063C-5254-00F0-0D60-000000000070", "event_uuid": "424E0D67-C4BF-2415-3978-670200000010", "event_type": "EVENT_CONNECT", "event_timestamp": 1523553424221490754, "subject_uuid": "283847BC-0200-0000-0000-000000000020", "subject_name": "mail", "object_uuid": "80370C6E-D2AA-9534-C617-500000000040", "object_path": "149.52.198.23 : 80"}
```
