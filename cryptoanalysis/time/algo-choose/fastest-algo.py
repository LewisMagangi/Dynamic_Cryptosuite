import sys

def compare_algorithm_speed():
    try:
        # Reading AES total time
        with open('aes_total_time.txt', 'r') as aes_file:
            aes_time = float(aes_file.read().strip())
            print("AES Total Time:", aes_time, "seconds")

        # Reading ECC total time
        with open('ecc_elapsed_time.txt', 'r') as ecc_file:
            ecc_time = float(ecc_file.read().strip())
            print("ECC Total Time:", ecc_time, "seconds")

        # Reading ECDSA total time
        with open('ecdsa_verification_time.txt', 'r') as ecdsa_file:
            ecdsa_time = float(ecdsa_file.read().strip())
            print("ECDSA Total Time:", ecdsa_time, "seconds")

        # Reading ECDH-AES total time
        with open('ecdh_aes_total_time.txt', 'r') as ecdh_aes_file:
            ecdh_aes_time = float(ecdh_aes_file.read().strip())
            print("ECDH-AES Total Time:", ecdh_aes_time, "seconds")

        # Comparing times
        fastest_algorithm = min(aes_time, ecc_time, ecdsa_time, ecdh_aes_time)
        if fastest_algorithm == aes_time:
            return "AES is the fastest algorithm."
        elif fastest_algorithm == ecc_time:
            return "ECC is the fastest algorithm."
        elif fastest_algorithm == ecdsa_time:
            return "ECDSA is the fastest algorithm."
        else:
            return "ECDH-AES is the fastest algorithm."
    except FileNotFoundError:
        return "One or more files not found."

def main():
   
    result = compare_algorithm_speed()
    print(result)
if __name__ == "__main__":
    main()
