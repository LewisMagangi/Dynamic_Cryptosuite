import scrypt
import os
import time
import sys

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

# Function for scrypt key derivation
def scrypt_derivation(password_bytes, salt):
    N = 16384
    r = 8
    p = 1
    return scrypt.hash(password_bytes, salt, N, r, p)

# Main function
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 scrypt_key_derivation.py <password_file>")
        sys.exit(1)

    password_file = sys.argv[1]
    password_bytes = read_file(password_file)

    if password_bytes is None:
        sys.exit(1)

    # Generating salt
    salt = os.urandom(16)

    # Derive key using scrypt
    start_time = time.time()
    derived_key = scrypt_derivation(password_bytes, salt)
    end_time = time.time()

    print(f"scrypt Derived Key: {derived_key.hex()}")
    print(f"Execution time: {end_time - start_time:.12f} seconds")

if __name__ == "__main__":
    main()
