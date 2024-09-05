import numpy as np
import time
import torch
from tqdm import tqdm
import re
import gensim
import sys
from gensim.models import KeyedVectors
sys.path.append('/home/yangyangwei/RAPiDLe/log_producer')
from theia.config import event_csv_list, event_npy_list, event_csv_predict_list, log_list

max_position_size = 10
count = 0
all_words = set()
zero_vector = np.zeros(100)

def load_raw_data(file_path): 
    events = []
    with open(file_path, 'r') as file:
        for line in tqdm(file, desc="Loading data"):
            events.append(line.strip())
    print(f"End of loading data>> the number of events: {len(events)}\n")
    return events

def parse_triplet(triplet_str):
    subject, operator, obj = triplet_str.split(', ')
    subject = subject.strip()
    operator = operator.strip()
    obj = obj.strip()
    return subject, operator, obj

def clean_text(text):
    # words = re.sub(r'/', ' ', text).split()  
    words = text.split(' ', 1)
    
    def file_case():
        words = text.split(' ', 1)
        return [word for word in words if word]

    def network_case():
        words = text.split()
        return [words[1]] + [words[2]]

    def process_case():
        words = text.split(' ', 1)
        return [word for word in words if word]
    
    def default_case():
        words = text.split(' ', 1)
        return ['relationship']

    switch = {
        "File": file_case,
        "Network": network_case,
        "Process": process_case
    }

    return switch.get(words[0], default_case)()

def get_position_vector(position, vector_size):
    angle_rads = position / np.power(10000, (2 * (np.arange(vector_size) // 2)) / np.float32(vector_size))
    angle_rads[0::2] = np.sin(angle_rads[0::2])  
    angle_rads[1::2] = np.cos(angle_rads[1::2])  
    return angle_rads

def get_vector(word):
    global all_words
    global zero_vector
    if word in all_words:
        return word_vectors[word]
    else:
        return zero_vector

def get_word_vector(words):
    vectors = []
    for i, word in enumerate(words):
        vector = get_vector(word)
        vectors.append(vector)

    if np.array_equal(vectors[1], zero_vector):
        vectors[0] = zero_vector
    if np.array_equal(vectors[4], zero_vector):
        vectors[3] = zero_vector
    vectors_matrix = np.array(vectors)
    return vectors_matrix.flatten()

def encode_triplet(triplet_str):

    subject, operator, obj = parse_triplet(triplet_str)
    
    subject = clean_text(subject)
    operator = clean_text(operator)
    obj = clean_text(obj)
    
    event_words = []
    event_words.extend(subject)
    event_words.extend(operator)
    event_words.extend(obj)

    if len(event_words) != 5:
        print(f"Event words length is : {triplet_str}")
        event_words = event_words[:5]
        sys.exit(1)

    event_vector = get_word_vector(event_words)
    return event_vector

def batch_encode_events(events, batch_size=128, save_path_prefix='encoded_events'):
    vectors = []

    for i in tqdm(range(0, len(events), batch_size), desc="Encoding events"):
        batch_events = events[i:i + batch_size]
        batch_vectors = [encode_triplet(event) for event in batch_events]
        vectors.append(batch_vectors)

    encoded_events = np.vstack(vectors)
    np.save(save_path_prefix, encoded_events)
    print(f"End of encoding events>> the shape of encoded events: {encoded_events.shape}\n") 

if __name__ == '__main__':
    word_vectors_path = '/home/yangyangwei/Baseline_Frequency/theia/data/word_vectors.kv'

    # malicious_test_data = '/home/yangyangwei/dataset/e3_cadets_preparation_event_2.csv'
    # malicious_test_data_npy = '/home/yangyangwei/dataset/e3_cadets_preparation_event_2.npy'

    batch_size = 1024

    # malicious_events = load_raw_data(malicious_test_data)

    
    word_vectors = KeyedVectors.load(word_vectors_path)
    all_words = set(word_vectors.index_to_key)
    zero_vector = np.zeros(word_vectors.vector_size)
    print('End of loading FastText model')

    encode_start_time = time.time()

    for csv_file, npy_file in zip(event_csv_list, event_npy_list):
        events = load_raw_data(csv_file)
        batch_encode_events(events, batch_size, save_path_prefix=npy_file)
        print(f"Encoding {csv_file} to {npy_file}")
    # batch_encode_events(malicious_events, batch_size, save_path_prefix=malicious_test_data_npy)
    
    encode_end_time = time.time()
    print(f"Time of encoding event data in {encode_end_time - encode_start_time:.2f} seconds")

    print(f'The number of key errors are: {count}')