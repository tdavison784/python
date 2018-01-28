#!/usr/bin/python
import json

def readJson(filename):
    """funtion to read and dump json"""
    with open(filename, 'r') as f_obj:
        numbers = json.load(f_obj)
    f_obj.close()
    msg = "Loaded File Content.. Displaying now... "
    print(msg, numbers)

readJson("numbers.json")