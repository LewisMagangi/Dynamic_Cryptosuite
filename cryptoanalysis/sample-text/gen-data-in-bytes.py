import os
from faker import Faker

def generate_text_data(size_in_bytes):
    text = ''
    text_generator = Faker()
    while len(text.encode('utf-8')) < size_in_bytes:
        remaining_bytes = size_in_bytes - len(text.encode('utf-8'))
        chunk_size = min(remaining_bytes, 1024)  # Chunk size of 1024 bytes or remaining bytes, whichever is smaller
        text += text_generator.text()
    return text

# Define ranges for text data generation
size_ranges = [(0, 256), (256, 512), (512, 1024), (1024, 2048), (2048, 4096)]  # Ranges in bytes

# Generate text data for each range and save it into a separate file
for size_range in size_ranges:
    text_data = generate_text_data(size_range[1])  # Generate data up to the upper bound of the range
    file_name = f"{size_range[0]}_{size_range[1]}_bytes_text_data_faker.txt"
    with open(file_name, 'w') as file:
        file.write(text_data)
    print(f"Generated text data in range {size_range[0]} - {size_range[1]} bytes using faker and saved it into {file_name}")
