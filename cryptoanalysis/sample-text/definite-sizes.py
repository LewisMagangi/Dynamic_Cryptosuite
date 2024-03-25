import os
import string

def generate_text_data(size_in_bytes):
    # Generate a string of random alphanumeric characters
    text = ''.join(string.ascii_letters + string.digits for _ in range(size_in_bytes))
    # If the generated text is larger than the required size, truncate it
    if len(text.encode('utf-8')) > size_in_bytes:
        text = text[:size_in_bytes]
    return text

# Define sizes for text data generation
sizes = [64, 128, 256, 512,]  # Sizes in bytes

# Generate text data for each size and overwrite the existing files
for size in sizes:
    text_data = generate_text_data(size)
    file_name = f"{size}_bytes_text_data.txt"
    with open(file_name, 'w') as file:
        file.write(text_data)
    print(f"Generated {size} bytes of text data and overwrote {file_name}")