import random
import string

def digitcode(length=15):
    characters = string.ascii_uppercase+string.ascii_lowercase + string.digits  # A-Z and 0-9
    code = ''.join(random.choices(characters, k=length))
    return code

# Example usage:
print(digitcode())  # Example output: G4X1Q9
