import sys
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.exceptions import InvalidSignature
import time

def sign_and_verify(message):
    # Generate RSA key pair
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

    # Convert message to bytes
    data = message.encode('utf-8')

    print(message)
    # Sign the data
    start_time = time.time()
    signature = private_key.sign(
        data,
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    end_time = time.time()
    signing_time = end_time - start_time
    print("Signing Time:", signing_time, "seconds")

    # Verify the signature
    try:
        public_key = private_key.public_key()
        start_time = time.time()
        public_key.verify(
            signature,
            data,
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        end_time = time.time()
        verification_time = end_time - start_time
        print("Signature is valid.")
        print("Verification Time:", verification_time, "seconds")
    except InvalidSignature:
        print("Signature is invalid.")

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            file_content = file.read()
        return file_content
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_name>")
        sys.exit(1)

    file_name = sys.argv[1]
    message = read_file(file_name)
    if message is None:
        sys.exit(1)

    sign_and_verify(message)
