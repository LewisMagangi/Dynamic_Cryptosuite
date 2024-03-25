import os
from mimesis import Text

def generate_text_data(size_in_mb):
    text = ''
    size_in_bytes = size_in_mb * 1024 * 1024  # Convert MB to bytes
    text_generator = Text()
    while len(text.encode('utf-8')) < size_in_bytes:
        remaining_bytes = size_in_bytes - len(text.encode('utf-8'))
        chunk_size = min(remaining_bytes, 1024)  # Chunk size of 1024 bytes or remaining bytes, whichever is smaller
        text += text_generator.text(quantity=chunk_size // 1000)  # Adjusting quantity based on bytes
    return text

# Sizes to generate text data for
sizes = [1, 2, 5, 10, 20, 50, 100]

# Generate text data for each size and save it into a separate file
for size in sizes:
    text_data = generate_text_data(size)
    file_name = f"{size}mb_text_data_mimesis.txt"
    with open(file_name, 'w', encoding='utf-8') as file:  # Specify encoding for writing Unicode characters
        file.write(text_data)
    print(f"Generated {size}MB of text data using Mimesis and saved it into {file_name}")
