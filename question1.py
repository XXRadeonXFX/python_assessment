"""
Q1. In DevOps, security is a crucial aspect, and ensuring strong passwords is essential. Create a Python script to check the strength of the password. 

(*) Implement a Python function called check_password_strength that takes a password string as input.
(*) The function should check the password against the following criteria:
(*) Minimum length: The password should be at least 8 characters long.
(*) Contains both uppercase and lowercase letters.
(*) Contains at least one digit (0-9).
(*) Contains at least one special character (e.g., !, @, #, $, %).
(*) The function should return a boolean value indicating whether the password meets the criteria.
(*) Write a script that takes user input for a password and calls the check_password_strength function to validate it.
(*) Provide appropriate feedback to the user based on the strength of the password.  
"""
import re

def check_password_strength(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter."
    if not re.search(r'[a-z]', password):
        return False, "Password must contain at least one lowercase letter."
    if not re.search(r'[0-9]', password):
        return False, "Password must contain at least one digit."
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "Password must contain at least one special character."
    return True, "Password is strong."

def main():
    password = input("Enter your password: ")
    is_valid, feedback = check_password_strength(password)
    if is_valid:
        print("Success! Your password is strong.")
    else:
        print(f"Error: {feedback}")

if __name__ == "__main__":
    main()