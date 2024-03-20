from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import sys

def encrypt_decrypt_rsa(original_message, key_size=2048):
    # Check if the key size is valid
    if key_size not in [1024, 2048, 3072, 4096]:
        print("Error: Invalid key size. Supported key sizes are 1024, 2048, 3072, or 4096.")
        sys.exit(1)

    # Generate RSA key pair with the specified key size
    key = RSA.generate(key_size)

    print(key)

    # Get the public and private key
    public_key = key.publickey()
    private_key = key

    # Encrypt the message using the public key
    cipher = PKCS1_OAEP.new(public_key)
    encrypted_message = cipher.encrypt(original_message.encode())
    print(encrypted_message)

    # Decrypt the message using the private key
    cipher = PKCS1_OAEP.new(private_key)
    decrypted_message = cipher.decrypt(encrypted_message)

    return decrypted_message.decode()

if __name__ == "__main__":
    # Check if any arguments are provided
    if len(sys.argv) > 1:
        original_message = sys.argv[1]
    else:
        # Use a default message if no arguments provided
        original_message = "Hi how are you ?"

    key_size = int(sys.argv[2]) if len(sys.argv) > 2 else 2048

    # Perform encryption and decryption with RSA
    try:
        decrypted_message = encrypt_decrypt_rsa(original_message, key_size)
        print("Original message:", original_message)
        print("Decrypted message:", decrypted_message)
    except ValueError:
        print("Error: Invalid key size. Supported key sizes are 1024, 2048, 3072, or 4096.")