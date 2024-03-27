
import subprocess
import sys

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, _ = process.communicate()
    return output.decode()

def run_crypto_analysis_scripts(input_file):
    scripts = [
        f"python aes-time.py {input_file}",
        f"python ecdh-aes-time.py {input_file}",
        f"python ecc-time.py {input_file}",
        f"python ecdsa-dig-time.py {input_file}"
        # Add more scripts if needed
    ]

    for script in scripts:
        print(f"Running script: {script}")
        output = run_command(script)
        print(output)

def main():
    if len(sys.argv) != 2:
        print("Usage: python run-algo-script.py <file_path>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    print("Running Crypto Analysis Scripts:")
    run_crypto_analysis_scripts(input_file)

if __name__ == "__main__":
    main()
