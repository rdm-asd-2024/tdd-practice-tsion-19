import re
import json
import csv

class PasswordValidator:
    def __init__(self, custom_validators=None):
        self.custom_validators = custom_validators if custom_validators else []
    
    def is_valid(self, password):
        # Check length
        if not 8 <= len(password) <= 16:
            return False, "Password length must be between 8 and 16 characters."
        
        # Check for uppercase letter and digit
        if not any(char.isupper() for char in password) or not any(char.isdigit() for char in password):
            return False, "Password must have at least one uppercase letter and one digit."
        
        # Check for at least 4 distinct characters
        if len(set(password)) < 4:
            return False, "Password must have at least 4 distinct characters."
        
        # Check for adjacent characters
        if any(password[i] == password[i+1] for i in range(len(password) - 1)):
            return False, "Password can't contain adjacent characters."
        
        # Apply custom validators
        for validator in self.custom_validators:
            if not validator(password):
                return False, "Custom validation failed."

        return True, "Password is valid."

def custom_validator_example(password):
    # Add your custom validation logic here
    # Return True if the password is valid, False otherwise
    return True

def main():
    # Create a PasswordValidator instance with custom validators
    validator = PasswordValidator(custom_validators=[custom_validator_example])

    # Example: Using JSON input
    json_data = [
        {"password": "Pass1234"},
        {"password": "Invalid"},
    ]
    for data in json_data:
        is_valid, message = validator.is_valid(data["password"])
        print(f"Password: {data['password']} - Valid: {is_valid} - Reason: {message}")

    # Example: Using CSV input
    csv_file = "passwords.csv"
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            is_valid, message = validator.is_valid(row["password"])
            print(f"Password: {row['password']} - Valid: {is_valid} - Reason: {message}")
if __name__ == "__main__":
    main()
