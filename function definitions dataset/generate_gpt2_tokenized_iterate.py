import itertools
from transformers import GPT2Tokenizer

# Initialize GPT-2 tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# Function to check token count of a given string
def token_count(text):
    return len(tokenizer.encode(text))

# Generate potential values for B
characters = "abcdefghijklmnopqrstuvwxyz"
valid_Bs = []

# Generate values for B (exactly 1 token)
for i in range(2, 4):  # Try lengths from 2 to 3 characters
    for combo in itertools.product(characters, repeat=i):
        B_candidate = "".join(combo)
        if token_count(B_candidate) == 1:
            valid_Bs.append(B_candidate)
        if len(valid_Bs) >= 1000:
            break
    if len(valid_Bs) >= 1000:
        break

# Generate function definitions and save to file
samples = [f'def iterate({B}):\n\t' for B in valid_Bs]

# Write all samples to a file
output_filename = "gpt2_tokenized_iterate_B1.txt"
with open(output_filename, "w") as file:
    for sample in samples:
        file.write(sample + "\n")

print(f"1000 function definitions written to {output_filename}")
