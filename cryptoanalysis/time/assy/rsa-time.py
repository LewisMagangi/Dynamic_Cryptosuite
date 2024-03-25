from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import sys
import time

def encrypt_decrypt_rsa(original_message, key_size=2048, iterations=2):
    # Generate RSA key pair with the specified key size
    key = RSA.generate(key_size)

    # Get the public and private key
    public_key = key.publickey()
    private_key = key

    # Initialize lists to store times for each iteration
    encryption_times = []
    decryption_times = []
    for _ in range(iterations):
        # Encrypt the message using the public key
        cipher = PKCS1_OAEP.new(public_key)
        # Encrypt the message and record the encryption time
        start_encrypt_time = time.time()
        encrypted_message = cipher.encrypt(original_message.encode())
        end_encrypt_time = time.time()
        encryption_times.append(end_encrypt_time - start_encrypt_time)

        # Decrypt the message using the private key
        cipher = PKCS1_OAEP.new(private_key)

        start_decrypt_time = time.time()
        decrypted_message = cipher.decrypt(encrypted_message)
        end_decrypt_time = time.time()
        decryption_times.append(end_decrypt_time - start_decrypt_time)

    # Calculate average encryption and decryption times
    average_encryption_time = sum(encryption_times) / iterations
    average_decryption_time = sum(decryption_times) / iterations

    return decrypted_message.decode(), average_encryption_time, average_decryption_time

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def main():
    # Check if any arguments are provided
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_file> [key_size]")
        sys.exit(1)

    input_file = sys.argv[1]
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
        decrypted_message, avg_encryption_time, avg_decryption_time = encrypt_decrypt_rsa(plaintext, key_size)

        # Print results
        print("Average encryption time:", avg_encryption_time)
        print("Average decryption time:", avg_decryption_time)

    except Exception as e:
        print("Error:", e)

    # Record the end time
    end_total_time = time.time()
    print("Total execution time:", end_total_time - start_total_time, "seconds")

if __name__ == "__main__":
    main()
