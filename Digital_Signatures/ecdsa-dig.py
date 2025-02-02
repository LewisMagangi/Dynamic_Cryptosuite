import sys
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend

def sign_and_verify(data):
    # Generate ECDSA key pair
    private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
    public_key = private_key.public_key()

    # Sign the data
    signature = private_key.sign(data, ec.ECDSA(hashes.SHA256()))

    # Verify the signature
    try:
        public_key.verify(signature, data, ec.ECDSA(hashes.SHA256()))
        print("Signature is valid.")
    except InvalidSignature:
        print("Signature is invalid.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 ecdsa-dig.py <data_to_be_signed>")
        sys.exit(1)

    data = sys.argv[1].encode('utf-8')  # Convert data to bytes
    sign_and_verify(data)
