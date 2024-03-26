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

    time_data.append((script_name, None, None))

    return time_data

def run_crypto_analysis_scripts(scripts):
    all_script_names = []
    all_time_data = []

    for script in scripts:
        print(f"Running script: {script}")
        output = run_command(script)
        print(output)
        time_data = extract_time_data(output, script)
        all_time_data.append(time_data)
        all_script_names.append(script)

    return list(zip(all_script_names, all_time_data))

def find_fastest_algorithm(results):
    encryption_times = [(t[1], name) for name, t in results if 'encryption' in name]
    decryption_times = [(t[1], name) for name, t in results if 'decryption' in name]

    fastest_encryption_time = min(encryption_times)[0]
    fastest_decryption_time = min(decryption_times)[0]

    encryption_scripts = [name for name, t in encryption_times if t == fastest_encryption_time]
    decryption_scripts = [name for name, t in decryption_times if t == fastest_decryption_time]

    fastest_algorithm = encryption_scripts[0] if fastest_encryption_time < fastest_decryption_time else decryption_scripts[0]

    return fastest_algorithm

if __name__ == "__main__":
    file_path = "your_file_path_here"
    scripts = [
        f"python {file_path} aes-speed-data.py",
        f"python {file_path} ecdh-speed-data.py",
        f"python {file_path} ecc-speed-data.py"
    ]

    results = run_crypto_analysis_scripts(scripts)
    fastest_algorithm = find_fastest_algorithm(results)
    print(f"The fastest algorithm is {fastest_algorithm}")