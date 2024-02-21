from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend

# Generate ECDSA key pair
private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
public_key = private_key.public_key()

# Data to be signed
data = b"Hello, this is some data to be signed."

# Sign the data
signature = private_key.sign(data, ec.ECDSA(hashes.SHA256()))

# Verify the signature
try:
    public_key.verify(signature, data, ec.ECDSA(hashes.SHA256()))
    print("Signature is valid.")
except InvalidSignature:
    print("Signature is invalid.")
