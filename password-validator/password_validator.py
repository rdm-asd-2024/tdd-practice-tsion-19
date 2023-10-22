# password_validator.py

class PasswordValidator:
    def __init__(self, min_length=8, max_length=20, allowed_chars=None, forbidden_words=None):
        self.min_length = min_length
        self.max_length = max_length
        self.allowed_chars = allowed_chars or set()
        self.forbidden_words = forbidden_words or []

    def is_valid(self, password):
        # Check minimum and maximum length
        if len(password) < self.min_length or len(password) > self.max_length:
            return False

        # Check allowed characters
        if any(char not in self.allowed_chars for char in password):
            return False

        # Check for forbidden words
        if any(word in password for word in self.forbidden_words):
            return False

        return True

def compose_criteria(criteria_list):
    def validate(password):
        for criteria in criteria_list:
            if not criteria.is_valid(password):
                return False
        return True
    return validate
