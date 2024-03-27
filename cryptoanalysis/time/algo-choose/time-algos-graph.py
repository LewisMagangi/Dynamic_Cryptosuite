import numpy as np
import matplotlib.pyplot as plt
import os

# Function to read the elapsed time from a file
def read_time(file_name):
    try:
        with open(file_name, 'r') as file:
            time = float(file.read().strip())
        return time
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return None

# Function to create a graph from the elapsed times
def create_graph(times, labels):
    plt.figure(figsize=(10, 5))
    plt.bar(labels, times, color='skyblue')
    plt.title('Elapsed Time for Encryption and Signature Verification Algorithms')
    plt.xlabel('Algorithm')
    plt.ylabel('Time (seconds)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # List of file names and their corresponding algorithms
    files = [
        ('aes_total_time.txt', 'AES'),
        ('ecc_elapsed_time.txt', 'ECC'),
        ('ecdh_aes_total_time.txt', 'ECDH-AES'),
        ('ecdsa_total-time.txt', 'ECDSA')
    ]

    # Read the times and labels from the files
    times = []
    labels = []
    for file_name, label in files:
        time = read_time(file_name)
        if time is not None:
            times.append(time)
            labels.append(label)

    # Create the graph
    create_graph(times, labels)
