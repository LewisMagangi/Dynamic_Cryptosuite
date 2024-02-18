from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes

def pad(data):
    # Pad the data to be a multiple of 8 bytes
    padding_length = 8 - len(data) % 8
    padding = bytes([padding_length]) * padding_length
    return data + padding

def unpad(data):
    # Remove padding from the data
    padding_length = data[-1]
    return data[:-padding_length]

def generate_key():
    # Generate a random Triple DES key
    return get_random_bytes(24)

def encrypt_message(message, key):
    cipher = DES3.new(key, DES3.MODE_ECB)
    padded_message = pad(message.encode('utf-8'))
    ciphertext = cipher.encrypt(padded_message)
    return ciphertext

def decrypt_message(ciphertext, key):
    cipher = DES3.new(key, DES3.MODE_ECB)
    padded_message = cipher.decrypt(ciphertext)
    message = unpad(padded_message).decode('utf-8')
    return message

# Example usage:
key = generate_key()
message = "Hello, this is a secret message to illustrate how triple des works."

# Encrypt the message
ciphertext = encrypt_message(message, key)
print("Ciphertext:", ciphertext)

# Decrypt the message
decrypted_message = decrypt_message(ciphertext, key)
print("Decrypted Message:", decrypted_message)
