from src.encoder.encoding_map import binary_to_char

class Encoder:
    def __init__(self):
        pass
    
    def int_to_binary_padded(self,n):
        binary = f"{n:b}"  # Convert to binary without '0b' prefix
        padding_length = (6 - len(binary) % 6) % 6  # Calculate how many leading zeros to add
        padded_binary = "0" * padding_length + binary  # Pad with leading zeros
        return padded_binary

    def get_short_string(self,num):
        padded_binary_string = self.int_to_binary_padded(num)
        chunks = [padded_binary_string[i:i+6] for i in range(0, len(padded_binary_string), 6)]
        encoded_string = ''.join(binary_to_char[chunk] for chunk in chunks)
        return encoded_string

encoder = Encoder()