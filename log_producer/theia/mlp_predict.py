import numpy as np
import pickle
import time
import torch
import sys
sys.path.append('path/RAPiDLe/log_producer')
from theia.config import event_csv_list, event_npy_list, event_csv_predict_list

def load_raw_data(raw_file_path):
    events = []
    with open(raw_file_path, 'r') as f:
        for line in f:
            events.append(line.strip())
    return events

def load_input_data(data_path):
    input_data = np.load(data_path, allow_pickle=True)
    return input_data

if __name__ == '__main__':

    batch_size = 1024
    
    # Load MLP model 
    with open('path/Baseline_Frequency/theia/data/mlp_model.pkl', 'rb') as file:
        mlp_model = pickle.load(file)
    print("Loaded MLP model")

    #Predict values for new events
    # X_test = load_input_data(test_path)

    # start_time = time.time()

    # y_pred_test = mlp_model.predict(X_test)

    # end_time = time.time()
    # print(f"Time of predicting event data in {end_time - start_time:.2f} seconds")
    # print(f"Predicted values for {len(y_pred_test)} new events, with average speed of {len(y_pred_test)  / (end_time - start_time):.2f} events per second")
    # malicious_event = load_raw_data('path/dataset/e3_cadets_preparation_event_2.csv')

    # with open(output_value_path, 'w') as csv_file:
    #     for event, prediction in zip(malicious_event, y_pred_test):
    #         csv_file.write(f"{event}, {prediction}\n")

    for npy_file, csv_file, predict_file in zip(event_npy_list, event_csv_list, event_csv_predict_list):
        # Load input data
        X_test = load_input_data(npy_file)

        start_time = time.time()

        # Predict values for new events
        y_pred_test = mlp_model.predict(X_test)

        end_time = time.time()
        print(f"Time of predicting event data in {end_time - start_time:.2f} seconds")
        print(f"Predicted values for {len(y_pred_test)} new events, with average speed of {len(y_pred_test) / (end_time - start_time):.2f} events per second")

        # Load raw event data
        malicious_event = load_raw_data(csv_file)

        # Save predictions to the corresponding CSV file
        with open(predict_file, 'w') as output_csv_file:
            for event, prediction in zip(malicious_event, y_pred_test):
                output_csv_file.write(f"{event}, {prediction}\n")
