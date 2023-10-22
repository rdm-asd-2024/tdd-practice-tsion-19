# cli.py

import json
import argparse
from password_validator import PasswordValidator, compose_criteria  # Import the PasswordValidator class

def load_criteria_from_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    criteria_list = []

    for criterion in data:
        criteria = PasswordValidator(**criterion)
        criteria_list.append(criteria)

    return compose_criteria(criteria_list)

def main():
    parser = argparse.ArgumentParser(description="Password Validator CLI")
    parser.add_argument("password", type=str, help="Password to validate")
    parser.add_argument("criteria_file", type=str, help="JSON file containing validation criteria")

    args = parser.parse_args()
    criteria_validator = load_criteria_from_file(args.criteria_file)
    if criteria_validator(args.password):
        print("Password is valid")
    else:
        print("Password is invalid")
