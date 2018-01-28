#!/usr/bin/python
import json


def data_info():
    """Function that will gather users name
    and favorite number. Function will save
    user info as a dictionary and save to a
    JSON file for later reference."""

    data = {}

    data['name'] = input("Enter your name: ")
    data['number'] = input("Enter your favorite number: ")

    return data


def save_info(filename):
    """Function that will save user info to a file"""
    info = user_info()

    with open(filename, 'w') as f_obj:
        json.dump(info, f_obj)
    f_obj.close()


def check_existance(filename):
    """Function that will check file
    to see if user exists.

    exists = True
    else:
        False"""
    #user_data = user_info()


    with open(filename, 'r') as f_obj:
        info = json.load(f_obj)
    f_obj.close()

    if user_data['name'] in info:
        print("User already exists.\n")
        print("Here is the info we have stored: ")
        print(user_data)

save_info("userinfo.json")
check_existance("userinfo.json")