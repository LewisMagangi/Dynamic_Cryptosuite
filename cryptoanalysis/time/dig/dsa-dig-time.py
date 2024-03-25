def sign_and_verify(data="Default data to be signed"):
    # Generate DSA key pair
    key = DSA.generate(2048)

    # Convert data to bytes
    data_bytes = data.encode('utf-8')

    # Sign the data
    hash_func = SHA256.new(data_bytes)
    start_time = time.time()
    signer = DSS.new(key, 'fips-186-3')
    signature = signer.sign(hash_func)
    end_time = time.time()
    signing_time = "{:.6f}".format(end_time - start_time)
    print("Signing Time:", signing_time, "seconds")

    # Verify the signature
    verifier = DSS.new(key.publickey(), 'fips-186-3')
    start_time = time.time()
    try:
        verifier.verify(hash_func, signature)
        print("Signature is valid.")
    except (ValueError, TypeError):
        print("Signature is invalid.")
    end_time = time.time()
    verification_time = "{:.6f}".format(end_time - start_time)
    print("Verification Time:", verification_time, "seconds")