import bcrypt

password = b'my_password'
salt = bcrypt.gensalt()

hashed_password = bcrypt.hashpw(password, salt)

# print the hashed password
print('Hashed Password:', hashed_password)
print("bcrypt Hashed Password:", hashed_password.decode())