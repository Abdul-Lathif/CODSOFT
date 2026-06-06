# Password Generator Program
# Created during CodSoft Virtual Internship

import random
import string

print("=== PASSWORD GENERATOR ===")

length = int(input("Enter password length: "))

# Combine letters, numbers, and symbols
characters = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choice(characters) for i in range(length))

print(f"Generated Password: {password}")