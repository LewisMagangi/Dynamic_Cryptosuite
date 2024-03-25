from Crypto.Signature import DSS
from Crypto.Hash import SHA256
from Crypto.PublicKey import DSA
import time
import sys

def sign_and_verify(data):
    # Generate DSA key pair
    key = DSA.generate(2048)

    # Convert data to bytes
    data_bytes = data.encode('utf-8')

    # Sign the data
    hash_func = SHA256.new(data_bytes)
    start_time_sign = time.time()
    signer = DSS.new(key, 'fips-186-3')
    signature = signer.sign(hash_func)
    end_time_sign = time.time()
    signing_time = end_time_sign - start_time_sign
    print("Signing Time:", "{:.6f}".format(signing_time), "seconds")
    #print(data)

    # Verify the signature
    verifier = DSS.new(key.publickey(), 'fips-186-3')
    start_time_verify = time.time()
    try:
        verifier.verify(hash_func, signature)
        print("Signature is valid.")
    except (ValueError, TypeError):
        print("Signature is invalid.")
    end_time_verify = time.time()
    verification_time = end_time_verify - start_time_verify
    print("Verification Time:", "{:.6f}".format(verification_time), "seconds")

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            file_content = file.read()
        return file_content
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return None

if __name__ == "__main__":
    start_time_program = time.time()
    if len(sys.argv) != 2:
        print("Usage: python3 dsa-dig-time.py [file_name]")
        sys.exit(1)

    file_name = sys.argv[1]
    data = read_file(file_name)
    if data is None:
        sys.exit(1)
    
    sign_and_verify(data)
    #print(data)
    end_time_program = time.time()
    program_runtime = end_time_program - start_time_program
    print("Total Program Runtime:", "{:.6f}".format(program_runtime), "seconds")
