import subprocess

# Define the file paths
file_paths = [
    ("1mb", "../cryptoanalysis/sample-text/1mb_text_data_faker.txt"),
    ("2mb", "../cryptoanalysis/sample-text/2mb_text_data_faker.txt"),
    ("5mb", "../cryptoanalysis/sample-text/5mb_text_data_faker.txt"),
    ("10mb", "../cryptoanalysis/sample-text/10mb_text_data_faker.txt"),
    ("20mb", "../cryptoanalysis/sample-text/20mb_text_data_faker.txt"),
    ("50mb", "../cryptoanalysis/sample-text/50mb_text_data_faker.txt")
]

# Loop through each file path and execute the Python script with memory profiling
for size, file_path in file_paths:
    print(f"Running script for {size} file: {file_path}")
    result = subprocess.run(["python", "-m", "memory_profiler", "ecc-time-mem.py", file_path], capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)
    
print("All scripts executed.")
