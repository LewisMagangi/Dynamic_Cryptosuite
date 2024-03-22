import hashlib
import time
import sys

def sha224(data="Default data to be hashed"):
    start_time = time.time()
    hashed_data = hashlib.sha224(data.encode()).hexdigest()
    end_time = time.time()
    print("Time taken for SHA-224:", end_time - start_time, "seconds")
    return hashed_data

def sha256(data="Default data to be hashed"):
    start_time = time.time()
    hashed_data = hashlib.sha256(data.encode()).hexdigest()
    end_time = time.time()
    print("Time taken for SHA-256:", end_time - start_time, "seconds")
    return hashed_data

def sha384(data="Default data to be hashed"):
    start_time = time.time()
    hashed_data = hashlib.sha384(data.encode()).hexdigest()
    end_time = time.time()
    print("Time taken for SHA-384:", end_time - start_time, "seconds")
    return hashed_data

def sha512(data="Default data to be hashed"):
    start_time = time.time()
    hashed_data = hashlib.sha512(data.encode()).hexdigest()
    end_time = time.time()
    print("Time taken for SHA-512:", end_time - start_time, "seconds")
    return hashed_data

def sha512_224(data="Default data to be hashed"):
    start_time = time.time()
    hashed_data = hashlib.sha512(data.encode()).hexdigest()[:56]
    end_time = time.time()
    print("Time taken for SHA-512/224:", end_time - start_time, "seconds")
    return hashed_data

def sha512_256(data="Default data to be hashed"):
    start_time = time.time()
    hashed_data = hashlib.sha512(data.encode()).hexdigest()[:64]
    end_time = time.time()
    print("Time taken for SHA-512/256:", end_time - start_time, "seconds")
    return hashed_data

def sha3_224(data="Default data to be hashed"):
    start_time = time.time()
    hashed_data = hashlib.sha3_224(data.encode()).hexdigest()
    end_time = time.time()
    print("Time taken for SHA3-224:", end_time - start_time, "seconds")
    return hashed_data

def sha3_256(data="Default data to be hashed"):
    start_time = time.time()
    hashed_data = hashlib.sha3_256(data.encode()).hexdigest()
    end_time = time.time()
    print("Time taken for SHA3-256:", end_time - start_time, "seconds")
    return hashed_data

def sha3_384(data="Default data to be hashed"):
    start_time = time.time()
    hashed_data = hashlib.sha3_384(data.encode()).hexdigest()
    end_time = time.time()
    print("Time taken for SHA3-384:", end_time - start_time, "seconds")
    return hashed_data

def sha3_512(data="Default data to be hashed"):
    start_time = time.time()
    hashed_data = hashlib.sha3_512(data.encode()).hexdigest()
    end_time = time.time()
    print("Time taken for SHA3-512:", end_time - start_time, "seconds")
    return hashed_data

def shake128(data="Default data to be hashed", output_length=32):
    start_time = time.time()
    hashed_data = hashlib.shake_128(data.encode()).hexdigest(output_length)
    end_time = time.time()
    print("Time taken for SHAKE128:", end_time - start_time, "seconds")
    return hashed_data

def shake256(data="Default data to be hashed", output_length=32):
    start_time = time.time()
    hashed_data = hashlib.shake_256(data.encode()).hexdigest(output_length)
    end_time = time.time()
    print("Time taken for SHAKE256:", end_time - start_time, "seconds")
    return hashed_data

def usage():
    print("Usage: python script.py [data_to_be_hashed]. If no data is provided, default data will be hashed.")

if __name__ == "__main__":
    if len(sys.argv) > 2:
        usage()
        sys.exit(1)

    data = sys.argv[1] if len(sys.argv) == 2 else "Hello World!"
    #print("Data to be hashed:", data)
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
