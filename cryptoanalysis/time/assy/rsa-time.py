from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import sys
import time

def encrypt_decrypt_rsa(original_message, key_size=2048):
    # Generate RSA key pair with the specified key size
    key = RSA.generate(key_size)

    # Get the public and private key
    public_key = key.publickey()
    private_key = key

    # Encrypt the message using the public key
    cipher = PKCS1_OAEP.new(public_key)

    # Encrypt the message and record the encryption time
    start_encrypt_time = time.time()
    encrypted_message = cipher.encrypt(original_message.encode())
    end_encrypt_time = time.time()
    encryption_time = end_encrypt_time - start_encrypt_time

    # Decrypt the message using the private key
    cipher = PKCS1_OAEP.new(private_key)

    start_decrypt_time = time.time()
    decrypted_message = cipher.decrypt(encrypted_message)
    end_decrypt_time = time.time()
    decryption_time = end_decrypt_time - start_decrypt_time

    return decrypted_message.decode(), encryption_time, decryption_time

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

if __name__ == "__main__":
    # Check if any arguments are provided
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        print("Usage: python script.py <input_file>")
        sys.exit(1)

    key_size = int(sys.argv[2]) if len(sys.argv) > 2 else 2048

    # Record the start time for both reading and encryption
    start_total_time = time.time()

    # Read plaintext from file
    start_read_time = time.time()
    plaintext = read_file(input_file)
    end_read_time = time.time()
    read_time = end_read_time - start_read_time

    # Perform encryption and decryption with RSA
    try:
        decrypted_message, encryption_time, decryption_time = encrypt_decrypt_rsa(plaintext, key_size)
        #print("Original message:", plaintext)
        #print("Decrypted message:", decrypted_message)
        print("Time taken to read plaintext:", read_time)
        print("Encryption time:", encryption_time)
        print("Decryption time:", decryption_time)
    except Exception as e:
        print("Error:", e)

    # Record the end time
    end_total_time = time.time()
    print("Total execution time:", end_total_time - start_total_time, "seconds")
