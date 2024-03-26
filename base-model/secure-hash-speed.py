import sys
import hashlib
import time

def sha224(data):
    start_time = time.time()
    _ = hashlib.sha224(data.encode()).hexdigest()
    end_time = time.time()
    return end_time - start_time

def sha256(data):
    start_time = time.time()
    _ = hashlib.sha256(data.encode()).hexdigest()
    end_time = time.time()
    return end_time - start_time

def sha384(data):
    start_time = time.time()
    _ = hashlib.sha384(data.encode()).hexdigest()
    end_time = time.time()
    return end_time - start_time

def sha512(data):
    start_time = time.time()
    _ = hashlib.sha512(data.encode()).hexdigest()
    end_time = time.time()
    return end_time - start_time

def sha512_224(data):
    start_time = time.time()
    _ = hashlib.sha512(data.encode()).hexdigest()[:56]
    end_time = time.time()
    return end_time - start_time

def sha512_256(data):
    start_time = time.time()
    _ = hashlib.sha512(data.encode()).hexdigest()[:64]
    end_time = time.time()
    return end_time - start_time

def sha3_224(data):
    start_time = time.time()
    _ = hashlib.sha3_224(data.encode()).hexdigest()
    end_time = time.time()
    return end_time - start_time

def sha3_256(data):
    start_time = time.time()
    _ = hashlib.sha3_256(data.encode()).hexdigest()
    end_time = time.time()
    return end_time - start_time

def sha3_384(data):
    start_time = time.time()
    _ = hashlib.sha3_384(data.encode()).hexdigest()
    end_time = time.time()
    return end_time - start_time

def sha3_512(data):
    start_time = time.time()
    _ = hashlib.sha3_512(data.encode()).hexdigest()
    end_time = time.time()
    return end_time - start_time

def shake128(data, output_length=32):
    start_time = time.time()
    _ = hashlib.shake_128(data.encode()).hexdigest(output_length)
    end_time = time.time()
    return end_time - start_time

def shake256(data, output_length=32):
    start_time = time.time()
    _ = hashlib.shake_256(data.encode()).hexdigest(output_length)
    end_time = time.time()
    return end_time - start_time

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

    file_paths = [
        ("1mb", "..\\cryptoanalysis\\sample-text\\1mb_text_data_faker.txt"),
        ("2mb", "..\\cryptoanalysis\\sample-text\\2mb_text_data_faker.txt"),
        ("5mb", "..\\cryptoanalysis\\sample-text\\5mb_text_data_faker.txt"),
        ("10mb", "..\\cryptoanalysis\\sample-text\\10mb_text_data_faker.txt"),
        ("20mb", "..\\cryptoanalysis\\sample-text\\20mb_text_data_faker.txt"),
        ("50mb", "..\\cryptoanalysis\\sample-text\\50mb_text_data_faker.txt"),
    ]

    print("Data Size {0: <10} Hash Algorithm {1: <10} Time (seconds)".format("", ""))
    print("-" * 45)

    for size, file_path in file_paths:
        data = read_file(file_path)
        if data is None:
            continue

        print(f"{size} {0: <10}", end="")
        algorithms = [
            ("SHA-224", sha224),
            ("SHA-256", sha256),
            ("SHA-384", sha384),
            ("SHA-512", sha512),
            ("SHA-512/224", sha512_224),
            ("SHA-512/256", sha512_256),
            ("SHA3-224", sha3_224),
            ("SHA3-256", sha3_256),
            ("SHA3-384", sha3_384),
            ("SHA3-512", sha3_512),
            ("SHAKE128", shake128),
            ("SHAKE256", shake256)
        ]

        for algorithm, hash_func in algorithms:
            elapsed_time = hash_func(data)
            print("{0: <15} {1: <10}".format(algorithm, elapsed_time))
