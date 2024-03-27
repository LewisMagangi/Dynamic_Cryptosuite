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
    plt.title('Elapsed Time for Different Hashing Algorithms')
    plt.xlabel('Hashing Algorithm')
    plt.ylabel('Time (seconds)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # List of file names and their corresponding hashing algorithms
    files = [
        ('sha224.txt', 'SHA-224'),
        ('sha256.txt', 'SHA-256'),
        ('sha384.txt', 'SHA-384'),
        ('sha3_224.txt', 'SHA3-224'),
        ('sha3_256.txt', 'SHA3-256'),
        ('sha3_384.txt', 'SHA3-384'),
        ('sha3_512.txt', 'SHA3-512'),
        ('sha512.txt', 'SHA-512'),
        ('sha512_224.txt', 'SHA-512/224'),
        ('sha512_256.txt', 'SHA-512/256'),
        ('shake128.txt', 'SHAKE128'),
        ('shake256.txt', 'SHAKE256')
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
