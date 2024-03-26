
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import sys
import time

def read_and_store_file(file_path):
    try:
        with open(file_path, 'r') as file:
            file_contents = file.read()
        return file_contents
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file '{file_path}': {e}")
        return None

def aes_gcm_encrypt(message, key):
    cipher = AES.new(key, AES.MODE_GCM)
    start_time = time.time()
    ciphertext, tag = cipher.encrypt_and_digest(message.encode())
    end_time = time.time()
    encryption_time = end_time - start_time
    return ciphertext, cipher.nonce, tag, encryption_time

def aes_gcm_decrypt(ciphertext, key, nonce, tag):
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    start_time = time.time()
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    end_time = time.time()
    decryption_time = end_time - start_time
    return plaintext.decode(), decryption_time

def main():
    file_paths = [
        ("1mb", "..\\cryptoanalysis\\sample-text\\1mb_text_data_faker.txt"),
        ("2mb", "..\\cryptoanalysis\\sample-text\\2mb_text_data_faker.txt"),
        ("5mb", "..\\cryptoanalysis\\sample-text\\5mb_text_data_faker.txt"),
        ("10mb", "..\\cryptoanalysis\\sample-text\\10mb_text_data_faker.txt"),
        ("20mb", "..\\cryptoanalysis\\sample-text\\20mb_text_data_faker.txt"),
        ("50mb", "..\\cryptoanalysis\\sample-text\\50mb_text_data_faker.txt"),
    ]

    print(f"Algorithm {chr(9)} Data Size {chr(9)} | AES Encryption Time (seconds) {chr(9)} | AES Decryption Time (seconds)")

    for i, (size, file_path) in enumerate(file_paths, start=1):
        start_time = time.time()

        plaintext = read_and_store_file(file_path)
        if plaintext is None:
            print(f"Error handling file ({size}): Unable to read file.")
            continue

        # Generate random key for AES encryption
        aes_key = get_random_bytes(16)  # 128-bit key

        # Encrypt data with AES
        ciphertext, nonce, tag, encryption_time = aes_gcm_encrypt(plaintext, aes_key)

        # Decrypt data with AES
        decrypted_text, decryption_time = aes_gcm_decrypt(ciphertext, aes_key, nonce, tag)

        elapsed_time = time.time() - start_time
        print(f"AES {chr(9)} {size} {chr(9)} | {encryption_time} {chr(9)} | {decryption_time}")

if __name__ == "__main__":
    main()
