from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# NIST-approved AES modes
nist_approved_modes = ["CBC", "CTR", "GCM", "CCM"]

def aes_encrypt(message, key, mode, nonce=None):
    if mode in nist_approved_modes:
        cipher = None
        if mode == "CBC":
            if nonce is None:
                print("Error: Nonce is required for CBC mode.")
                return None
            cipher = AES.new(key, AES.MODE_CBC, nonce)
        elif mode == "CTR":
            if nonce is None:
                print("Error: Nonce is required for CTR mode.")
                return None
            cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
        elif mode == "GCM":
            if nonce is None:
                print("Error: Nonce is required for GCM mode.")
                return None
            cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
        elif mode == "CCM":
            if nonce is None:
                print("Error: Nonce is required for CCM mode.")
                return None
            cipher = AES.new(key, AES.MODE_CCM, nonce=nonce)

        if cipher:
            if mode in ["GCM", "CCM"]:
                ciphertext, tag = cipher.encrypt_and_digest(message)
                return ciphertext, cipher.nonce, tag
            else:
                ciphertext = cipher.encrypt(pad(message, AES.block_size))
                return ciphertext
    else:
        print("Error: Mode '{}' is not NIST-approved.".format(mode))
        print("Valid NIST-approved modes are:", nist_approved_modes)
        return None

def aes_decrypt(ciphertext, key, mode, nonce=None, tag=None):
    if mode in nist_approved_modes:
        cipher = None
        if mode == "CBC":
            if nonce is None:
                print("Error: Nonce is required for CBC mode.")
                return None
            cipher = AES.new(key, AES.MODE_CBC, nonce)
        elif mode == "CTR":
            if nonce is None:
                print("Error: Nonce is required for CTR mode.")
                return None
            cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
        elif mode == "GCM":
            if nonce is None or tag is None:
                print("Error: Nonce and tag are required for GCM mode.")
                return None
            cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
        elif mode == "CCM":
            if nonce is None or tag is None:
                print("Error: Nonce and tag are required for CCM mode.")
                return None
            cipher = AES.new(key, AES.MODE_CCM, nonce=nonce)

        if cipher:
            if mode in ["GCM", "CCM"]:
                plaintext = cipher.decrypt_and_verify(ciphertext, tag)
                return plaintext
            else:
                decrypted = cipher.decrypt(ciphertext)
                return unpad(decrypted, AES.block_size)
    else:
        print("Error: Mode '{}' is not NIST-approved.".format(mode))
        print("Valid NIST-approved modes are:", nist_approved_modes)
        return None

# Example usage:
key = b'Sixteen byte key'
nonce = b'Random IV'
message = b'Hello, AES!'

# Specify the mode here
mode = "ECB"

# Encrypt
ciphertext, nonce_out, tag = aes_encrypt(message, key, mode, nonce)
if ciphertext:
    print("Ciphertext:", ciphertext)
    print("Nonce:", nonce_out)
    print("Tag:", tag)

# Decrypt
if mode in ["GCM", "CCM"]:
    plaintext = aes_decrypt(ciphertext, key, mode, nonce_out, tag)
else:
    plaintext = aes_decrypt(ciphertext, key, mode, nonce_out)

if plaintext:
    print("Plaintext:", plaintext.decode())
