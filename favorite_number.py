#!/usr/bin/python
import json


def get_stored_number():
    """Function to get stored number if available"""
    filename = "favorite_number.json"
    try:
        with open(filename, 'r') as f_obj:
            number = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return number


def get_new_number():
    """Function to store favorite number"""
    filename = "favorite_number.json"
    number = input("Please enter your favorite number: ")
    with open(filename, 'w') as f_obj:
        json.dump(number, f_obj)
        f_obj.close()

def present_number():
    """Function to print favorite number"""
    number = get_stored_number()

    if number:
        print("I know your favorite number: ", number)
    else:
        create_number = get_new_number()
        print("I know your favorite number: ", create_number)

present_number()