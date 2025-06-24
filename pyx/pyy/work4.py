import os
import string
import time
import random

PASSWORD_FILE = "password.txt"

def store_password():
    password = input("Create a password (8-15 characters): ")
    if len(password) < 8:
        return "Password is too short. Must be at least 8 characters."
    elif len(password) > 15:
        return "Password is too long. Must be at most 15 characters."
        
    with open(PASSWORD_FILE, "w") as file:
        file.write(password)
    
    return "Password stored successfully!"

def brute_force():
    """Simple brute force algorithm for password reset demonstration"""
    if not os.path.exists(PASSWORD_FILE):
        print("No password file found.")
        return False
    print
    with open(PASSWORD_FILE, "r") as file:
        stored_password = file.read().strip()
    
    print("Attempting to recover password...")
    print("This is a simulation of password recovery.")
    
    # Show a "hacking" animation to simulate brute force
    chars = string.ascii_letters + string.digits + string.punctuation
    attempts = 0
    password_length = len(stored_password)
    
    # Display some fake attempts
    for i in range(10):
        fake_attempt = ''.join(random.choice(chars) for _ in range(password_length))
        attempts += 1
        print(f"Attempt {attempts}: {fake_attempt}", end='\r')
        time.sleep(0.3)
    
    # Show progress bar
    print("\nAnalyzing password pattern...\n")
    for i in range(0, 101, 10):
        progress = "█" * (i // 10)
        spaces = " " * (10 - (i // 10))
        print(f"Progress: [{progress}{spaces}] {i}%", end='\r')
        time.sleep(0.2)
    
    print("\n\nPassword cracked!")
    print(f"Your password is: {stored_password}")
    
    choice = input("\nWould you like to reset your password? (y/n): ").lower()
    if choice == 'y':
        new_password = input("Enter new password (8-15 characters): ")
        while len(new_password) < 8 or len(new_password) > 15:
            if len(new_password) < 8:
                print("Password is too short. Must be at least 8 characters.")
            else:
                print("Password is too long. Must be at most 15 characters.")
            new_password = input("Enter new password (8-15 characters): ")
            
        with open(PASSWORD_FILE, "w") as file:
            file.write(new_password)
        print("Password reset successfully!")
        return True
    else:
        print("Password remains unchanged.")
        return False

def verify_password():
    # Checks if the user has entered the correct password
    if not os.path.exists(PASSWORD_FILE):
        print("No password is set. Please create one first.")
        return False
        
    entered_password = input("Enter your password: ")
    
    with open(PASSWORD_FILE, "r") as file:
        stored_password = file.read().strip()
    
    if entered_password == stored_password:
        print("Access Granted!")
        return True
    else:
        print("Incorrect Password. Try again.")
        return False

def main():
    # Main function to handle password storage and verification
    if not os.path.exists(PASSWORD_FILE):
        print("🔹 No password found. Let's create one!")
        result = store_password()
        print(result)
    else:
        choice = input("Do you want to (L)ogin or (F)orgot Password? ").lower()
        
        if choice == "l":
            verify_password()
        elif choice == "f":
            brute_force()
        else:
            print("Invalid choice .")

if __name__ == "__main__":
    main()