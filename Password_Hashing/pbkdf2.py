import hashlib
import os

password = b'my_password'
salt = os.urandom(16)
iterations = 100000  # Adjust as needed

derived_key = hashlib.pbkdf2_hmac('sha256', password, salt, iterations)

print("PBKDF2 Derived Key:", derived_key.hex())
