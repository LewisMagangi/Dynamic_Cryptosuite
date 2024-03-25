import sys
import hashlib
import time

def sha224(data):
    start_time = time.time()
    hashed_data = hashlib.sha224(data.encode()).hexdigest()
    end_time = time.time()
    print("Time taken for SHA-224:", end_time - start_time, "seconds")
    return hashed_data

def sha256(data):
    start_time = time.time()
    hashed_data = hashlib.sha256(data.encode()).hexdigest()
    end_time = time.time()
    print("Time taken for SHA-256:", end_time - start_time, "seconds")
    return hashed_data

def sha384(data):
    start_time = time.time()
    hashed_data = hashlib.sha384(data.encode()).hexdigest()
    end_time = time.time()
    print("Time taken for SHA-384:", end_time - start_time, "seconds")
    return hashed_data

def sha512(data):
    start_time = time.time()
    hashed_data = hashlib.sha512(data.encode()).hexdigest()
    end_time = time.time()
    print("Time taken for SHA-512:", end_time - start_time, "seconds")
    return hashed_data

def sha512_224(data):
    start_time = time.time()
    hashed_data = hashlib.sha512(data.encode()).hexdigest()[:56]
    end_time = time.time()
    print("Time taken for SHA-512/224:", end_time - start_time, "seconds")
    return hashed_data

def sha512_256(data):
    start_time = time.time()
    hashed_data = hashlib.sha512(data.encode()).hexdigest()[:64]
    end_time = time.time()
    print("Time taken for SHA-512/256:", end_time - start_time, "seconds")
    return hashed_data

def sha3_224(data):
    start_time = time.time()
    hashed_data = hashlib.sha3_224(data.encode()).hexdigest()
    end_time = time.time()
    print("Time taken for SHA3-224:", end_time - start_time, "seconds")
    return hashed_data

def sha3_256(data):
    start_time = time.time()
    hashed_data = hashlib.sha3_256(data.encode()).hexdigest()
    end_time = time.time()
    print("Time taken for SHA3-256:", end_time - start_time, "seconds")
    return hashed_data

def sha3_384(data):
    start_time = time.time()
    hashed_data = hashlib.sha3_384(data.encode()).hexdigest()
    end_time = time.time()
    print("Time taken for SHA3-384:", end_time - start_time, "seconds")
    return hashed_data

def sha3_512(data):
    start_time = time.time()
    hashed_data = hashlib.sha3_512(data.encode()).hexdigest()
    end_time = time.time()
    print("Time taken for SHA3-512:", end_time - start_time, "seconds")
    return hashed_data

def shake128(data, output_length=32):
    start_time = time.time()
    hashed_data = hashlib.shake_128(data.encode()).hexdigest(output_length)
    end_time = time.time()
    print("Time taken for SHAKE128:", end_time - start_time, "seconds")
    return hashed_data

def shake256(data, output_length=32):
    start_time = time.time()
    hashed_data = hashlib.shake_256(data.encode()).hexdigest(output_length)
    end_time = time.time()
    print("Time taken for SHAKE256:", end_time - start_time, "seconds")
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
