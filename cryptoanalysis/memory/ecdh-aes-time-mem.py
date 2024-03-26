import sys
import os
import time
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from memory_profiler import profile

@profile
def generate_key_pair():
    private_key = ec.generate_private_key(ec.SECP384R1(), default_backend())
    public_key = private_key.public_key()
    return private_key, public_key

@profile
def save_public_key(public_key):
    public_key_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    with open("public_key.pem", "wb") as f:
        f.write(public_key_pem)

@profile
def load_public_key():
    with open("public_key.pem", "rb") as f:
        public_key_pem = f.read()
    return serialization.load_pem_public_key(public_key_pem, backend=default_backend())

@profile
def derive_shared_key(private_key, public_key):
    shared_key = private_key.exchange(ec.ECDH(), public_key)
    return shared_key

@profile
def encrypt_file(file_path, shared_key):
    with open(file_path, "rb") as f:
        plaintext = f.read()

    # Derive AES key from shared key
    derived_key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b'aes_key',
        backend=default_backend()
    ).derive(shared_key)

    # Generate random IV
    iv = os.urandom(16)

    # Perform encryption with AES
    cipher = Cipher(algorithms.AES(derived_key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    # Write IV and ciphertext to file
    with open(file_path + ".enc", "wb") as f:
        f.write(iv)
        f.write(ciphertext)

@profile
def decrypt_file(file_path, shared_key):
    with open(file_path, "rb") as f:
        iv = f.read(16)
        ciphertext = f.read()

    # Derive AES key from shared key
    derived_key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b'aes_key',
        backend=default_backend()
    ).derive(shared_key)

    # Perform decryption with AES
    cipher = Cipher(algorithms.AES(derived_key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    # Write decrypted plaintext to file
    with open(file_path[:-4], "wb") as f:
        f.write(plaintext)

@profile
def main(file_path):
    start_time = time.time()

    private_key, public_key = generate_key_pair()
    save_public_key(public_key)
    shared_key = derive_shared_key(private_key, load_public_key())
    encrypt_file(file_path, shared_key)
    decrypt_file(file_path + ".enc", shared_key)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Elapsed time:", elapsed_time, "seconds")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)
    file_path = sys.argv[1]
    main(file_path)
