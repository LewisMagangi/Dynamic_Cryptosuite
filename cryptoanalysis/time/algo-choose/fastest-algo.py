import sys

def compare_algorithm_speed():
        try:
            with open('ecdsa_verification_time.txt', 'r') as ecdsa_file, open('ecc_elapsed_time.txt', 'r') as ecc_file:
                ecdsa_time = float(ecdsa_file.read().strip())
                ecc_time = float(ecc_file.read().strip())

                print("ECDSA time:", ecdsa_time, "seconds")
                print("ECC time:", ecc_time, "seconds")

                if ecdsa_time < ecc_time:
                    return "ECDSA is faster."
                elif ecc_time < ecdsa_time:
                    return "ECC is faster."
                else:
                    return "Both algorithms have the same speed."
        except FileNotFoundError:
            return "One or both files not found."

def main():
   
    result = compare_algorithm_speed()
    print(result)
if __name__ == "__main__":
    main()
