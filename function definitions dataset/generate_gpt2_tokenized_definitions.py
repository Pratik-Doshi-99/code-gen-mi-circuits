import itertools
import random
from transformers import GPT2Tokenizer

# Initialize GPT-2 tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# Function to check token count of a given string
def token_count(text):
    return len(tokenizer.encode(text))

# Generate potential values for A and B
characters = "abcdefghijklmnopqrstuvwxyz"

# Create lists to store valid values for A and B
valid_As = []
valid_Bs = []

# Generate values for A (exactly 2 tokens)
for i in range(2, 6):  # Try lengths from 2 to 5 characters
    for combo in itertools.product(characters, repeat=i):
        A_candidate = "".join(combo)
        if token_count(A_candidate) == 2:
            valid_As.append(A_candidate)

# Generate values for B (exactly 1 token)
for i in range(2, 4):  # Try lengths from 2 to 3 characters
    for combo in itertools.product(characters, repeat=i):
        B_candidate = "".join(combo)
        if token_count(B_candidate) == 1:
            valid_Bs.append(B_candidate)

# Generate function definitions with a total of 8 tokens
samples = []
for _ in range(1000):  # Generate 1000 samples
    while True:
        A = random.choice(valid_As)
        B = random.choice(valid_Bs)
        full_string = f"def {A}({B}):\n\t"
        if token_count(full_string) == 8:
            samples.append(full_string)
            break

# Write all samples to a file
with open("function_definitions_8_tokens.txt", "w") as file:
    for sample in samples:
        file.write(sample + "\n")

print("1000 function definitions written to function_definitions_8_tokens.txt")
