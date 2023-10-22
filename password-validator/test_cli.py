# test_cli.py

import unittest
import json
from unittest import mock
import sys
from io import StringIO
from cli import load_criteria_from_file, main  # Import functions and classes from the 'cli' module

class TestCLI(unittest.TestCase):
    def test_load_criteria_from_file(self):
        # Define data for this test
        data = [
            {"min_length": 8},
            {"allowed_chars": ["a", "b", "c"]}
        ]
        with mock.patch('builtins.open', mock.mock_open(read_data=json.dumps(data))):
            criteria = load_criteria_from_file("criteria.json")

        # Adjust this assertion based on the criteria defined in 'data'
        self.assertTrue(criteria("abcdefgh"))
        self.assertFalse(criteria("abc123"))

    def test_main(self):
        # Define data for this test
        data = [
            {"min_length": 8},
            {"allowed_chars": ["a", "b", "c"]}
        ]
        args = ["password123", "test_criteria.json"]
        with mock.patch.object(sys, 'argv', ["validate"] + args):
            with mock.patch('builtins.open', mock.mock_open(read_data=json.dumps(data))):
                with mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                    main()

                # Access the printed output as a string and assert its content
                output_contents = mock_stdout.getvalue()
                self.assertEqual(output_contents.strip(), "Password is valid")

if __name__ == '__main__':
    unittest.main()
