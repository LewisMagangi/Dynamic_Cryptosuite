from Crypto.PublicKey import ECC
from Crypto.Signature import DSS
from Crypto.Hash import SHA256
import sys

def generate_key_pair():
    key = ECC.generate(curve='P-256')
    return key

def save_key_pair(private_key, public_key):
    with open('private_key.pem', 'wb') as f:
        f.write(private_key.export_key(format='PEM'))
    with open('public_key.pem', 'wb') as f:
        f.write(public_key.export_key(format='PEM'))

def load_key_pair():
    with open('private_key.pem', 'rb') as f:
        private_key = ECC.import_key(f.read())
    with open('public_key.pem', 'rb') as f:
        public_key = ECC.import_key(f.read())
    return private_key, public_key

def sign_message(private_key, message):
    hash_message = SHA256.new(message)
    signer = DSS.new(private_key, 'fips-186-3')
    signature = signer.sign(hash_message)
    return signature

def verify_signature(public_key, message, signature):
    hash_message = SHA256.new(message)
    verifier = DSS.new(public_key, 'fips-186-3')
    try:
        verifier.verify(hash_message, signature)
        print("Signature is valid.")
    except ValueError:
        print("Signature is not valid.")

def main():
    if len(sys.argv) != 3:
        print("Usage: python ecc_encrypt.py <private_key_file> <message>")
        return

    private_key_file = sys.argv[1]
    message = sys.argv[2].encode('utf-8')

    private_key, public_key = generate_key_pair()
    save_key_pair(private_key, public_key)

    private_key, _ = load_key_pair()

    signature = sign_message(private_key, message)
    print("Signature:", signature.hex())

    _, public_key = load_key_pair()
    verify_signature(public_key, message, signature)

if __name__ == "__main__":
    main()
