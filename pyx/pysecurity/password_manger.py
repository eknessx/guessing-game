# the code is the main core to genrate random passwords and create ones
import random
import string
import os # Import the os module to check for file existence

# --- Configuration for Persistent Storage ---
PASSWORD_DATA = "data" 
data = set() #using sets is useful since we want to make a password and store it and to avoid any accidental typos

#its just a data loader function
def load_data():
    if os.path.exists(PASSWORD_DATA): # Check if the file exists
        with open(PASSWORD_DATA, 'r') as f:
            for line in f:
                password = line.strip() # Remove leading/trailing whitespace (like newline characters)
                if password: # Only add if the line isn't empty
                    data.add(password)
    print(f"Loaded {len(data)} passwords from '{PASSWORD_DATA}'") # For compiling

def save_passwords():
    """Saves all passwords from the 'data' set to the PASSWORD_FILE."""
    with open(PASSWORD_DATA, 'w') as f: # 'w' mode overwrites the file each time
        for password in data:
            f.write(password + '\n')
    print(f"Saved {len(data)} passwords to '{PASSWORD_DATA}'") # For debugging

load_data()

#the function that will alow you to create passwords and well UHH yeah
def password_algo(password_string):
    if password_string.isalnum():
        if password_string in data:
            return None, "This password already USED FOOL" #funny gta refrence line
        data.add(password_string)
        save_passwords() # <--- Save after adding a new password
        return password_string, "created successfully"
    else:
        return None, "LETTERS AND NUMBERS ONLY!."

#the function that creates random passwords
def algo_randomizer(length=8):
    #Generates a random alphanumeric password of a specified length.
    #Returns the generated password and a success message.
    if not isinstance(length, int) or length <= 0:
        return None, "Invalid length for password. THERE ARE LIMITS YOU KNOW?"

    alphabets = string.ascii_letters + string.digits
    
    # Loop until a unique password is generated (to avoid issues with small length or few chars)
    random_pass_ass = ''
    attempts = 0
    while random_pass in data and attempts < 100: # Limit attempts to avoid infinite loops for small char sets
        random_pass = ''.join(random.choices(alphabets, k=length))
        attempts += 1
    
    if random_pass_ass in data: # If after attempts, still not unique (highly unlikely for reasonable length)
        return None, "well that did not work OPPS."


    data.add(random_pass)
    save_passwords() # <--- Save after adding a new password
    return random_pass, f"New password generated: {random_pass}"

#function TO GET the list of stored password
def get_data():
    return sorted(list(data)) # Return sorted for easier viewing