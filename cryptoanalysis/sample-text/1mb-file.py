from faker import Faker

fake = Faker()

desired_size_bytes = 1024 * 1024 * 2 # 2 MB
generated_text = ''

while len(generated_text.encode('utf-8')) < desired_size_bytes:
    generated_text += fake.text()

# Trim excess characters to meet desired size exactly
generated_text = generated_text[:desired_size_bytes]

print(generated_text)
print("Generated text size:", len(generated_text.encode('utf-8')), "bytes")