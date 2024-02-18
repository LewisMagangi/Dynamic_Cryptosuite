from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def aes_gcm_encrypt(message, key):
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(message.encode())
    return ciphertext, cipher.nonce, tag

def aes_gcm_decrypt(ciphertext, key, nonce, tag):
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    return plaintext.decode()

# Example usage:
key = get_random_bytes(16)  # 128-bit key

def demo_aes_gcm_encrypt(key, message="This is an example message to illustrate how aes works"):
    ciphertext, nonce, tag = aes_gcm_encrypt(message, key)
    print("Ciphertext:", ciphertext)
    print("Nonce:", nonce)
    print("Tag:", tag)
    return ciphertext, nonce, tag

def demo_aes_gcm_decrypt(key, ciphertext, nonce, tag):
    plaintext = aes_gcm_decrypt(ciphertext, key, nonce, tag)
    print("Plaintext:", plaintext)
    return plaintext

# Example usage with demo text:
print("Encrypting demo text:")
ciphertext, nonce, tag = demo_aes_gcm_encrypt(key)

print("\nDecrypting demo text:")
demo_aes_gcm_decrypt(key, ciphertext, nonce, tag)
