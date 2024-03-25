import os
import sys
import time
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hmac
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
from base64 import b64encode

def generate_key_pair():
    keypair = rsa.generate_private_key(
        public_exponent=65537,
        key_size=4096,
        backend=default_backend()
    )

    return keypair

def save_public_key(public_key):
    public_pem = public_key.public_bytes(
        encoding=Encoding.PEM,
        format=PublicFormat.SubjectPublicKeyInfo
    )

    with open("public_key.pem", "wb") as file:
        file.write(public_pem)

def load_public_key():
    with open("public_key.pem", "rb") as file:
        public_bytes = file.read()

    public_key = rsa.import_key(public_bytes)

    return public_key

def encrypt_file(file_path, public_key):

    with open(file_path, "rb") as f:
        data = f.read()

    rsa_encryptor = public_key.encryptor(
        padding=rsa.padding.OAEP(
            mgf=rsa.padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    rsa_ciphertext = rsa_encryptor.update(data) + rsa_encryptor.finalize()

    ciphertext = b''
    HASH_SIZE = hashes.SHA256().digest_size

    h = hmac.new(hashes.SHA256(), rsa_ciphertext, hashes.SHA256())

    while True:
        size = min(len(data), 4 * HASH_SIZE)

        if len(data) > 4 * HASH_SIZE:
            h.update(data[:size])

        elif len(data) < 4 * HASH_SIZE:
            h.update(data)

        if size == 32:
            h.update(b'\x01')

        else:
            h.update(b'\x00')

        ciphertext += h.digest()

        if len(data) <= size:
            break

        data = data[size:]

    ciphertext += rsa_ciphertext

    key = os.urandom(32)

    iv = os.urandom(16)

    derived_key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b'aes_key',
        backend=default_backend()
    ).derive(key)

    aes_cipher = Cipher(algorithms.AES(derived_key), modes.CFB(iv), backend=default_backend())

    encryptor = aes_cipher.encryptor()

    ciphertext = encryptor.update(ciphertext) + encryptor.finalize()

    # Write IV, encrypted data, and encrypted RSA data
    with open(file_path + ".enc", "wb") as f:
        f.write(iv)
        f.write(ciphertext)
        f.write(b64encode(rsa_ciphertext))

def decrypt_file(file_path, private_key):

    with open(file_path, "rb") as f: