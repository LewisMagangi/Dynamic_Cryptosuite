import subprocess
import time

# File sizes in bytes
sizes = [1, 2, 4, 8, 16, 32, 64]

# Number of iterations
iterations = 100

# Dictionary to store average times for each file size
average_times = {}

# Loop through each file size
for size in sizes:
    total_execution_time = 0
    input_file = f"../sample-text/{size}_bytes_text_data_faker.txt"

    # Loop through 100 times
    for i in range(iterations):
        # Run the rsa-time.py script and capture its output
        start_time = time.time()
        result = subprocess.run(["python", "rsa-time.py", input_file, str(size)], capture_output=True, text=True)
        end_time = time.time()
        execution_time = end_time - start_time

        # Extract the total execution time from the output
        lines = result.stdout.split("\n")
        encryption_time = float(lines[0].split(":")[-1].strip())
        decryption_time = float(lines[1].split(":")[-1].strip())

        # Add the execution time to the total
        total_execution_time += execution_time + encryption_time + decryption_time

    # Calculate the average time for this file size
    average_time = total_execution_time / iterations
    average_times[size] = average_time

# Print the average times for each file size
for size, average_time in average_times.items():
    print(f"Average time for {size} bytes: {average_time} seconds")
