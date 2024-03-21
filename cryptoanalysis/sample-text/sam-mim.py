from mimesis import Text

# Create a Text object
text_generator = Text()

# Function to generate text data of approximately 1MB (in bytes)
def generate_1mb_text():
    text = ''
    size_in_bytes = 1024 * 1024  # 1MB in bytes
    while len(text.encode('utf-8')) < size_in_bytes:
        chunk_size = min(size_in_bytes - len(text.encode('utf-8')), 1024)  # Chunk size of 1024 bytes
        text += text_generator.text(quantity=1)
    return text

# Generate 1MB of text data
text_data = generate_1mb_text()

# Print information
print("Generated 1MB of text data")
print(f"Data Size: {len(text_data.encode('utf-8')) / (1024 * 1024)} MB")
 