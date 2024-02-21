import hashlib
from Crypto.Hash import SHAKE128, SHAKE256
from Crypto.Protocol.KDF import HKDF

def sha256(message=None, key_size=None):
    if message is None:
        message = b'Hello, World!'
    if key_size is None:
        key_size = 32
    hkdf = HKDF(hashlib.sha256, key_size, b'salt', b'info')
    hkdf.update(message)
    return hkdf.read(key_size)

def sha3_256(message=None, byte_size=None):
    if message is None:
        message = b'Hello, World!'
    if byte_size is None:
        byte_size = 32
    shake = hashlib.sha3_256()
    shake.update(message)
    return shake.digest(byte_size)

def shake128(message=None, byte_size=None):
    if message is None:
        message = b'Hello, World!'
    if byte_size is None:
        byte_size = 32
    shake = SHAKE128.new(data=message)
    return shake.read(byte_size)

def shake256(message=None, byte_size=None):
    if message is None:
        message = b'Hello, World!'
    if byte_size is None:
        byte_size = 32
    shake = SHAKE256.new(data=message)
    return shake.read(byte_size)

def main():
    print("SHA-256:", sha256())
    print("SHA3-256:", sha3_256())
    print("SHAKE128:", shake128())
    print("SHAKE256:", shake256())

if _name_ == "_main_":
    main()

print("SHA-256:", sha256(b'Hello, World!', 64))
print("SHA3-256:", sha3_256(b'Hello, World!', 64))
print("SHAKE128:", shake128(b'Hello, World!', 64))
print("SHAKE256:", shake256(b'Hello, World!', 64))