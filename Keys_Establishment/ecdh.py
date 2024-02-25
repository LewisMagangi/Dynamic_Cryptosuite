#Implementing ecdh in python and ensuring the code is nist compliant
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

# Generate private key
bob_private_key = ec.generate_private_key(ec.SECP384R1())

# Generate public key
bob_public_key = bob_private_key.public_key()

# Serialize public key
bob_public_key_pem = bob_public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Generate private key
alice_private_key = ec.generate_private_key(ec.SECP384R1())

# Generate public key
alice_public_key = alice_private_key.public_key()

# Serialize public key
alice_public_key_pem = alice_public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Alice and Bob exchange public keys

# Alice loads Bob's public key
bob_public_key_from_alice = ec.EllipticCurvePublicKey.from_pem(bob_public_key_pem)

# Bob loads Alice's public key
alice_public_key_from_bob = ec.EllipticCurvePublicKey.from_pem(alice_public_key_pem)

# Alice and Bob compute shared secrets
alice_shared_key = alice_private_key.exchange(ec.ECDH(), bob_public_key_from_alice)
bob_shared_key = bob_private_key.exchange(ec.ECDH(), alice_public_key_from_bob)

# Alice and Bob's shared secrets should be the same
assert alice_shared_key == bob_shared_key