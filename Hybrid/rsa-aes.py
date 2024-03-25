from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from base64 import b64encode
import os
import sys

def generate_key_pair():
    keypair = rsa.generate_private_key(
        public_exponent=65537,
        key_size=4096,
        backend=default_backend()
    )

    return keypair

def save_public_key(public_key):
    public_key_pem = public_key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    with open("public_key.pem", "wb") as f:
        f.write(public_key_pem)

def load_public_key():
    with open("public_key.pem", "rb") as f:
        public_key_pem = f.read()

    public_key = serialization.load_pem_public_key(
        public_key_pem,
        backend=default_backend()
    )

    return public_key

def encrypt_file(file_path, public_key):

    with open(file_path, "rb") as f:
        plaintext = f.read()

    # Encrypt RSA
    rsa_cipher = public_key.encrypt(
        plaintext,
        padding=rsa.padding.OAEP(
            mgf=rsa.padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Encrypt AES
    derived_key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b'aes_key',
        backend=default_backend()
    ).derive(rsa_cipher)

    # Generate random IV
    iv = os.urandom(16)

    # Perform encryption with AES
    aes_cipher = Cipher(algorithms.AES(derived_key), modes.CFB(iv), backend=default_backend())
    encryptor = aes_cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    # Write IV, encrypted RSA, and encrypted AES to file
    with open(file_path + ".enc", "wb") as f:
        f.write(iv)
        f.write(b64encode(rsa_cipher))
        f.write(ciphertext)

def decrypt_file(file_path, private_key):

    with open(file_path, "rb") as f:
        iv = f.read(16)
        rsa_cipher = b64encode(f.read(256))
        ciphertext = f.read()

    # Decrypt RSA
    rsa_plaintext = private_key.decrypt(
        rsa_cipher,
        padding=rsa.padding.OAEP(
            mgf=rsa.padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Derive AES key
    derived_key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b'aes_key',
        backend=default_backend()
    ).derive(rsa_plaintext)

    # Perform decryption with AES
    aes_cipher = Cipher(algorithms.AES(derived_key), modes.CFB(iv), backend=default