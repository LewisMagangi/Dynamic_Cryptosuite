import sys
import hashlib
import time

def sha224(data):
    start_time = time.time()
    hashed_data = hashlib.sha224(data.encode()).hexdigest()
    end_time = time.time()
    total_time = end_time - start_time
    print("Time taken for SHA-224:", total_time, "seconds")
    with open('sha224.txt', 'w') as elapsed_time_file:
        elapsed_time_file.write(str(total_time))
    return hashed_data

def sha256(data):
    start_time = time.time()
    hashed_data = hashlib.sha256(data.encode()).hexdigest()
    end_time = time.time()
    total_time = end_time - start_time
    with open('sha256.txt', 'w') as elapsed_time_file:
        elapsed_time_file.write(str(total_time))
    print("Time taken for SHA-256:", total_time, "seconds")
    return hashed_data

def sha384(data):
    start_time = time.time()
    hashed_data = hashlib.sha384(data.encode()).hexdigest()
    end_time = time.time()
    total_time = end_time - start_time
    with open('sha384.txt', 'w') as elapsed_time_file:
        elapsed_time_file.write(str(total_time))
    print("Time taken for SHA-384:", total_time, "seconds")
    return hashed_data

def sha512(data):
    start_time = time.time()
    hashed_data = hashlib.sha512(data.encode()).hexdigest()
    end_time = time.time()
    total_time = end_time - start_time
    with open('sha512.txt', 'w') as elapsed_time_file:
        elapsed_time_file.write(str(total_time))
    print("Time taken for SHA-512:", total_time, "seconds")
    return hashed_data

def sha512_224(data):
    start_time = time.time()
    hashed_data = hashlib.sha512(data.encode()).hexdigest()[:56]
    end_time = time.time()
    total_time = end_time - start_time
    with open('sha512_224.txt', 'w') as elapsed_time_file:
        elapsed_time_file.write(str(total_time))
    print("Time taken for SHA-512/224:", total_time, "seconds")
    return hashed_data

def sha512_256(data):
    start_time = time.time()
    hashed_data = hashlib.sha512(data.encode()).hexdigest()[:64]
    end_time = time.time()
    total_time = end_time - start_time
    with open('sha512_256.txt', 'w') as elapsed_time_file:
        elapsed_time_file.write(str(total_time))
    print("Time taken for SHA-512/256:", total_time, "seconds")
    return hashed_data

def sha3_224(data):
    start_time = time.time()
    hashed_data = hashlib.sha3_224(data.encode()).hexdigest()
    end_time = time.time()
    total_time = end_time - start_time
    with open('sha3_224.txt', 'w') as elapsed_time_file:
        elapsed_time_file.write(str(total_time))
    print("Time taken for SHA3-224:", total_time, "seconds")
    return hashed_data

def sha3_256(data):
    start_time = time.time()
    hashed_data = hashlib.sha3_256(data.encode()).hexdigest()
    end_time = time.time()
    total_time = end_time - start_time
    with open('sha3_256.txt', 'w') as elapsed_time_file:
        elapsed_time_file.write(str(total_time))
    print("Time taken for SHA3-256:", total_time, "seconds")
    return hashed_data

def sha3_384(data):
    start_time = time.time()
    hashed_data = hashlib.sha3_384(data.encode()).hexdigest()
    end_time = time.time()
    total_time = end_time - start_time
    with open('sha3_384.txt', 'w') as elapsed_time_file:
        elapsed_time_file.write(str(total_time))
    print("Time taken for SHA3-384:", total_time, "seconds")
    return hashed_data

def sha3_512(data):
    start_time = time.time()
    hashed_data = hashlib.sha3_512(data.encode()).hexdigest()
    end_time = time.time()
    total_time = end_time - start_time
    with open('sha3_512.txt', 'w') as elapsed_time_file:
        elapsed_time_file.write(str(total_time))
    print("Time taken for SHA3-512:", total_time, "seconds")
    return hashed_data

def shake128(data, output_length=32):
    start_time = time.time()
    hashed_data = hashlib.shake_128(data.encode()).hexdigest(output_length)
    end_time = time.time()
    total_time = end_time - start_time
    with open('shake128.txt', 'w') as elapsed_time_file:
        elapsed_time_file.write(str(total_time))
    print("Time taken for SHAKE128:", total_time, "seconds")
    return hashed_data

def shake256(data, output_length=32):
    start_time = time.time()
    hashed_data = hashlib.shake_256(data.encode()).hexdigest(output_length)
    end_time = time.time()
    total_time = end_time - start_time
    with open('shake256.txt', 'w') as elapsed_time_file:
        elapsed_time_file.write(str(total_time))
    print("Time taken for SHAKE256:", total_time, "seconds")
    return hashed_data

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            file_content = file.read()
        return file_content
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return None

def usage():
    print("Usage: python script.py [file_name]. If no file name is provided, default data will be hashed.")

if __name__ == "__main__":
    if len(sys.argv) > 2:
        usage()
        sys.exit(1)

    file_name = sys.argv[1] if len(sys.argv) == 2 else "example.txt"
    data = read_file(file_name)
    if data is None:
        sys.exit(1)

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
    print("SHAKE 128:", shake128(data))
    print("SHAKE 256:", shake256(data))
