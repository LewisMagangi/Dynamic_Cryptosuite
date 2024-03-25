import sys
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend
import time

def sign_and_verify(data):
    # Generate ECDSA key pair
    private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
    public_key = private_key.public_key()

    # Sign the data
    start_time = time.time()
    signature = private_key.sign(data, ec.ECDSA(hashes.SHA256()))
    end_time = time.time()
    signing_time = end_time - start_time
    print("Signing Time:", signing_time, "seconds")

    # Verify the signature
    try:
        start_time = time.time()
        public_key.verify(signature, data, ec.ECDSA(hashes.SHA256()))
        end_time = time.time()
        verification_time = end_time - start_time
        print("Signature is valid.")
        print("Verification Time:", verification_time, "seconds")
    except InvalidSignature:
        print("Signature is invalid.")

def read_file(file_name):
    try:
        with open(file_name, 'rb') as file:  # Opening file in binary mode to read bytes
            file_content = file.read()
        return file_content
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 ecdsa-dig.py <file_name>")
        sys.exit(1)

    file_name = sys.argv[1]
    data = read_file(file_name)
    if data is None:
        sys.exit(1)

    sign_and_verify(data)
