import subprocess
import re

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, _ = process.communicate()
    return output.decode()

def extract_time_data(output, script_name):
    time_data = []
    lines = output.split('\n')
    if script_name == "python aes-speed-data.py":
        for line in lines:
            match = re.search(r'AES\s+(\d+\w+)\s+\|\s+([0-9.]+)\s+\|\s+([0-9.]+)', line)
            if match:
                size = match.group(1)
                encryption_time = float(match.group(2))
                decryption_time = float(match.group(3))
                time_data.append((size, encryption_time, decryption_time))
    elif script_name == "python ecdh-speed-data.py":
        for line in lines:
            match = re.search(r'ECDH\s+(\d+\w+)\s+\|\s+([0-9.]+)', line)
            if match:
                size = match.group(1)
                time_taken = float(match.group(2))
                time_data.append((size, time_taken))
    elif script_name == "python ecc-speed-data.py":
        for line in lines:
            match = re.search(r'ECC\s+(\d+\w+)\s+\|\s+([0-9.]+)', line)
            if match:
                size = match.group(1)
                time_taken = float(match.group(2))
                time_data.append((size, time_taken))
    return time_data

def run_crypto_analysis_scripts():
    scripts = [
        "python aes-speed-data.py",
        "python ecdh-speed-data.py",
        "python ecc-speed-data.py"
        # Add more scripts if needed
    ]

    all_time_data = []

    for script in scripts:
        print(f"Running script: {script}")
        output = run_command(script)
        print(output)
        time_data = extract_time_data(output, script)
        all_time_data.append(time_data)
        #print(all_time_data)

    return all_time_data

if __name__ == "__main__":
    time_data = run_crypto_analysis_scripts()
    print("Time data from all scripts:")
    for idx, data in enumerate(time_data, 1):
        print(f"Script {idx}: {data}")
