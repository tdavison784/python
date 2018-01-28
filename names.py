#!/usr/bin/python

from name_function import get_formatted_name

def get_name():
    """Function that calls name from name_function module
    and prints results"""

    print("Enter q at any time to quit.")

    while True:
        first = input("Enter your first name: ")
        if first == "q":
            break
        last = input("Enter your last name: ")
        if last == "q":
            break

    formatted_name = get_formatted_name("tommy", "davison")
    print("Neatly formatted name: ", formatted_name)

get_name()

