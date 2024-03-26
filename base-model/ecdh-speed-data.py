from Crypto.PublicKey import ECC
from Crypto.Signature import DSS
from Crypto.Hash import SHA256
import sys
import time
import os

def generate_key_pair():
    private_key = ECC.generate(curve='P-256')
    public_key = private_key.public_key()
    return private_key, public_key

def save_key_pair(private_key, public_key):
    with open('private_key.pem', 'wb') as f:
        f.write(private_key.export_key(format='PEM').encode('utf-8'))
    with open('public_key.pem', 'wb') as f:
        f.write(public_key.export_key(format='PEM').encode('utf-8'))

def load_key_pair():
    with open('private_key.pem', 'rb') as f:
        private_key = ECC.import_key(f.read())
    with open('public_key.pem', 'rb') as f:
        public_key = ECC.import_key(f.read())
    return private_key, public_key

def sign_message(private_key, message):
    hash_message = SHA256.new(message)
    signer = DSS.new(private_key, 'fips-186-3')
    signature = signer.sign(hash_message)
    return signature

def verify_signature(public_key, message, signature):
    hash_message = SHA256.new(message)
    verifier = DSS.new(public_key, 'fips-186-3')
    try:
        verifier.verify(hash_message, signature)
    except ValueError:
        print("Signature is not valid.")

def main():
    file_paths = [
        ("1mb", "..\\cryptoanalysis\\sample-text\\1mb_text_data_faker.txt"),
        ("2mb", "..\\cryptoanalysis\\sample-text\\2mb_text_data_faker.txt"),
        ("5mb", "..\\cryptoanalysis\\sample-text\\5mb_text_data_faker.txt"),
        ("10mb", "..\\cryptoanalysis\\sample-text\\10mb_text_data_faker.txt"),
        ("20mb", "..\\cryptoanalysis\\sample-text\\20mb_text_data_faker.txt"),
        ("50mb", "..\\cryptoanalysis\\sample-text\\50mb_text_data_faker.txt"),
    ]

    print(f"Algorithm {chr(9)} Data Size {chr(9)} | Time Taken (seconds)")

    for i, (size, file_path) in enumerate(file_paths, start=1):
        start_time = time.time()

        private_key, public_key = generate_key_pair()
        save_key_pair(private_key, public_key)

        _, public_key = load_key_pair()

        try:
            with open(file_path, 'rb') as file:
                message = file.read()

            signature = sign_message(private_key, message)

        except Exception as e:
            print(f"Error handling file ({size}): {str(e)}")

        elapsed_time = time.time() - start_time
        print(f"ECC {chr(9)} {size} {chr(9)}   | {elapsed_time}")

if __name__ == "__main__":
    main()
