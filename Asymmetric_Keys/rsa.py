from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Generate RSA key pair
key = RSA.generate(2048)

# Get the public and private key
public_key = key.publickey()
private_key = key

# Encrypt a message using the public key
message = b"Hello, world!"
cipher = PKCS1_OAEP.new(public_key)
encrypted_message = cipher.encrypt(message)

# Decrypt the message using the private key
cipher = PKCS1_OAEP.new(private_key)
decrypted_message = cipher.decrypt(encrypted_message)

print("Original message:", message)
print("Decrypted message:", decrypted_message)
