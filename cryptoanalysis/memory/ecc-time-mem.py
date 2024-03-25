from Crypto.PublicKey import ECC
from Crypto.Signature import DSS
from Crypto.Hash import SHA256
import sys
import time
from memory_profiler import profile

@profile
def generate_key_pair():
    private_key = ECC.generate(curve='P-256')
    public_key = private_key.public_key()
    return private_key, public_key

@profile
def save_key_pair(private_key, public_key):
    with open('private_key.pem', 'wb') as f:
        f.write(private_key.export_key(format='PEM').encode('utf-8'))
    with open('public_key.pem', 'wb') as f:
        f.write(public_key.export_key(format='PEM').encode('utf-8'))

@profile
def load_key_pair():
    with open('private_key.pem', 'rb') as f:
        private_key = ECC.import_key(f.read())
    with open('public_key.pem', 'rb') as f:
        public_key = ECC.import_key(f.read())
    return private_key, public_key

@profile
def sign_message(private_key, message):
    hash_message = SHA256.new(message)
    signer = DSS.new(private_key, 'fips-186-3')
    signature = signer.sign(hash_message)
    return signature

@profile
def verify_signature(public_key, message, signature):
    hash_message = SHA256.new(message)
    verifier = DSS.new(public_key, 'fips-186-3')
    try:
        verifier.verify(hash_message, signature)
        print("Signature is valid.")
    except ValueError:
        print("Signature is not valid.")

@profile
def main():
    # Record the start time
    start_time = time.time()

    if len(sys.argv) != 2:
        print("Usage: python3 ecc.py <filename>")
        return

    filename = sys.argv[1]

    try:
        with open(filename, 'rb') as file:
            message = file.read()
    except FileNotFoundError:
        print("File not found.")
        return

    private_key, public_key = generate_key_pair()
    save_key_pair(private_key, public_key)

    _, public_key = load_key_pair()

    signature = sign_message(private_key, message)
    print("Signature:", signature.hex())

    verify_signature(public_key, message, signature)

    # Record the end time
    end_time = time.time()

    # Calculate elapsed time
    elapsed_time = end_time - start_time
    print("Total time taken:", elapsed_time, "seconds")

if __name__ == "__main__":
    main()
