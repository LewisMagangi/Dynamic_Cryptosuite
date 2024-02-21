from Crypto.Signature import DSS
from Crypto.Hash import SHA256
from Crypto.PublicKey import DSA

# Generate DSA key pair
key = DSA.generate(2048)

# Data to be signed
data = b"Hello, this is some data to be signed."

# Sign the data
hash_func = SHA256.new(data)
signer = DSS.new(key, 'fips-186-3')
signature = signer.sign(hash_func)

# Verify the signature
verifier = DSS.new(key.publickey(), 'fips-186-3')
try:
    verifier.verify(hash_func, signature)
    print("Signature is valid.")
except (ValueError, TypeError):
    print("Signature is invalid.")
