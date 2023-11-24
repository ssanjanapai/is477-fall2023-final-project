import os
import requests
import hashlib

def download_file(url, local_path):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        with open(local_path, mode='wb') as f:
            f.write(response.content)
        return True  # Download successful
    except requests.exceptions.RequestException as e:
        print(f"Error downloading file from {url}: {e}")
        return False  # Download failed

def calculate_sha256(file_path):
    with open(file_path, mode='rb') as f:
        data = f.read()
        sha256hash = hashlib.sha256(data).hexdigest()
        return sha256hash

# URL for the Car Evaluation dataset
dataset_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data"

# Local path for downloaded Car Evaluation dataset
car_evaluation_path = 'data/car_evaluation_dataset.csv'

# Download Car Evaluation dataset and check integrity
if download_file(dataset_url, car_evaluation_path):
    expected_hash = 'b703a9ac69f11e64ce8c223c0a40de4d2e9d769f7fb20be5f8f2e8a619893d83' 
    sha256hash_car_evaluation = calculate_sha256(car_evaluation_path)
    
    if expected_hash == sha256hash_car_evaluation:
        print('The Car Evaluation dataset has passed integrity check.')
    else:
        print('Hash does not match, integrity check failed on the Car Evaluation dataset.')
else:
    print('Error: Unable to download the Car Evaluation dataset.')
