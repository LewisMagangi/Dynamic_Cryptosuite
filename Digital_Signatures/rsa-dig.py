import sys
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.exceptions import InvalidSignature

def sign_and_verify(message):
    # Generate RSA key pair
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

    # Convert message to bytes
    data = message.encode('utf-8')

    # Sign the data
    signature = private_key.sign(
        data,
        padding.PKCS1v15(),
        hashes.SHA256()
    )

    # Verify the signature
    try:
        public_key = private_key.public_key()
        public_key.verify(
            signature,
            data,
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        print("Signature is valid.")
    except InvalidSignature:
        print("Signature is invalid.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <message_to_be_signed>")
        sys.exit(1)

    message = sys.argv[1]
    sign_and_verify(message)