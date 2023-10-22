# test_password_validator.py

import unittest
from password_validator import PasswordValidator, compose_criteria

class TestPasswordValidator(unittest.TestCase):
    def test_min_length(self):
        validator = PasswordValidator(min_length=6)
        self.assertTrue(validator.is_valid("123456"))
        self.assertFalse(validator.is_valid("12345"))

    # Add more tests for other criteria...

    def test_compose_criteria(self):
        criteria1 = PasswordValidator(min_length=6)
        criteria2 = PasswordValidator(allowed_chars={"a", "b", "c"})
        composed_validator = compose_criteria([criteria1, criteria2])

        self.assertTrue(composed_validator("123abc"))
        self.assertFalse(composed_validator("1234"))

if __name__ == '__main__':
    unittest.main()
