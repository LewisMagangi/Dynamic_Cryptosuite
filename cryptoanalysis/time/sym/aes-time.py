from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import time

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

# Example usage:
key = get_random_bytes(16)  # 128-bit key

# Encrypt data
message = "This is an example message to illustrate how aes works"
ciphertext, nonce, tag, encryption_time = aes_gcm_encrypt(message, key)
print("Ciphertext:", ciphertext)
print("Nonce:", nonce)
print("Tag:", tag)
print("Encryption Time:", encryption_time, "seconds")

# Decrypt data
plaintext, decryption_time = aes_gcm_decrypt(ciphertext, key, nonce, tag)
print("Plaintext:", plaintext)
print("Decryption Time:", decryption_time, "seconds")
