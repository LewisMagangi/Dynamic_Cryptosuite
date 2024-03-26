from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import sys
import time
from memory_profiler import profile

@profile
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

@profile
def aes_gcm_encrypt(message, key):
    cipher = AES.new(key, AES.MODE_GCM)
    start_time = time.time()
    ciphertext, tag = cipher.encrypt_and_digest(message.encode())
    end_time = time.time()
    encryption_time = end_time - start_time
    return ciphertext, cipher.nonce, tag, encryption_time

@profile
def aes_gcm_decrypt(ciphertext, key, nonce, tag):
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    start_time = time.time()
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    end_time = time.time()
    decryption_time = end_time - start_time
    return plaintext.decode(), decryption_time

@profile
def main():
    # Check if any arguments are provided
    if len(sys.argv) < 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)

    # Read file contents
    file_path = sys.argv[1]
    plaintext = read_and_store_file(file_path)
    if plaintext is None:
        print("Exiting due to error in reading the file.")
        sys.exit(1)

    # Generate random key for AES encryption
    aes_key = get_random_bytes(16)  # 128-bit key

    # Record the start time for the entire process
    start_total_time = time.time()

    # Encrypt data with AES
    ciphertext, nonce, tag, encryption_time = aes_gcm_encrypt(plaintext, aes_key)
    print("AES Encryption Time:", encryption_time, "seconds")

    # Decrypt data with AES
    decrypted_text, decryption_time = aes_gcm_decrypt(ciphertext, aes_key, nonce, tag)
    print("AES Decryption Time:", decryption_time, "seconds")

    # Record the end time
    end_total_time = time.time()
    print("Total execution time:", end_total_time - start_total_time, "seconds")

if __name__ == "__main__":
    main()
