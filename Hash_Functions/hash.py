import hashlib

def sha224(data):
    return hashlib.sha224(data).hexdigest()

def sha256(data):
    return hashlib.sha256(data).hexdigest()

def sha384(data):
    return hashlib.sha384(data).hexdigest()

def sha512(data):
    return hashlib.sha512(data).hexdigest()

def sha512_224(data):
    return hashlib.sha512(data).hexdigest()[:56]

def sha512_256(data):
    return hashlib.sha512(data).hexdigest()[:64]

def sha3_224(data):
    return hashlib.sha3_224(data).hexdigest()

def sha3_256(data):
    return hashlib.sha3_256(data).hexdigest()

def sha3_384(data):
    return hashlib.sha3_384(data).hexdigest()

def sha3_512(data):
    return hashlib.sha3_512(data).hexdigest()

def shake128(data, output_length):
    return hashlib.shake_128(data).hexdigest(output_length)

def shake256(data, output_length):
    return hashlib.shake_256(data).hexdigest(output_length)

# Example usage
data = b"Hello, world!"
print("SHA-224:", sha224(data))
print("SHA-256:", sha256(data))
print("SHA-384:", sha384(data))
print("SHA-512:", sha512(data))
print("SHA-512/224:", sha512_224(data))
print("SHA-512/256:", sha512_256(data))
print("SHA3-224:", sha3_224(data))
print("SHA3-256:", sha3_256(data))
print("SHA3-384:", sha3_384(data))
print("SHA3-512:", sha3_512(data))
print("SHAKE 128:", shake128(data, 32))
print("SHAKE 256:", shake256(data, 32))