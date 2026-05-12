import random

import string

def generate_password(length=12):
    if length < 4:
        return "Password length should be at least 4"

    # Character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    
    all_characters = lowercase + uppercase + digits + symbols
    password += random.choices(all_characters, k=length - 4)

    
    random.shuffle(password)

    return ''.join(password)

print("=== Password Generator ===")

try:
    length = int(input("Enter password length: "))
    password = generate_password(length)
    print("Generated Password:", password)

except ValueError:
    print("Please enter a valid number.")
