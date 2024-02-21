from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

# Generate RSA key pair
key = RSA.generate(2048)

# Data to be signed
data = b"Hello, this is some data to be signed."

# Sign the data
hash_func = SHA256.new(data)
signer = pkcs1_15.new(key)
signature = signer.sign(hash_func)

# Verify the signature
verifier = pkcs1_15.new(key.publickey())
try:
    verifier.verify(hash_func, signature)
    print("Signature is valid.")
except (ValueError, TypeError):
    print("Signature is invalid.")
