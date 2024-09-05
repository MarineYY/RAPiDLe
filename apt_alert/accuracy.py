def get_last_non_empty_line(file_path):
    last_non_empty_line = None
    with open(file_path, 'r') as file:
        for line in file:
            stripped_line = line.strip()
            if stripped_line:
                last_non_empty_line = stripped_line
    return last_non_empty_line

file_paths = [
    '/home/yangyangwei/RAPiDLe/apt_alert/frequency-3-test.log',
    '/home/yangyangwei/RAPiDLe/apt_alert/frequency-4-test.log',
    '/home/yangyangwei/RAPiDLe/apt_alert/frequency-5-test.log'
]

TP = 0
FP = 0
r1 = 0
r2 = 0

for file_path in file_paths:
    last_line = get_last_non_empty_line(file_path)
    print(f'Last non-empty line in {file_path}: {last_line}')

    last_line_parts = last_line.split(', ')
    TP += int(last_line_parts[2].split(': ')[1])
    FP += int(last_line_parts[3].split(': ')[1])
    r1 += int(last_line_parts[4].split(': ')[1])
    r2 += int(last_line_parts[5].split(': ')[1])

precision = TP / (TP + FP)
recall = r1 / r2
f1_score = 2 * (precision * recall) / (precision + recall)
print(f'Precision: {precision}, Recall: {recall}, F1 Score: {f1_score}')
