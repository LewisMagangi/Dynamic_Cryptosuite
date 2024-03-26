import bcrypt
import sys
import time

# Function for reading file content
def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            file_content = file.read()
            #print(file_content)
        return file_content
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return None

# Function for bcrypt password hashing
def bcrypt_hash_password(password):
    salt = bcrypt.gensalt()
    start_time = time.time()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    end_time = time.time()
    hashing_time = end_time - start_time
    return hashed_password, hashing_time

# Main function
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 my_bcrypt-time.py <password_file>")
        sys.exit(1)

    password_file = sys.argv[1]
    password_bytes = read_file(password_file)
    print(password_bytes)

    if password_bytes is None:
        sys.exit(1)

    # Hash password using bcrypt
    hashed_password, hashing_time = bcrypt_hash_password(password_bytes)

    # Print the hashed password
    print("bcrypt Hashed Password:", hashed_password.decode())
    print("Hashing Time:", hashing_time, "seconds")

if __name__ == "__main__":
    main()
