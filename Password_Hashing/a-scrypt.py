import scrypt
import os

password = b'my_password'
salt = os.urandom(16)
N = 16384
r = 8
p = 1

derived_key = scrypt.hash(password, salt, N, r, p)

print("scrypt Derived Key:", derived_key.hex())
