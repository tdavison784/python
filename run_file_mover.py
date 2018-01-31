#!/usr/bin/python
from get_files import FileMover

filename = "file.json"

## Inits get_files module and stores the filename used here into the module for usage
my_file = FileMover(filename)
## Loads all info from the "file.json" into a variable for later reference
my_file.store_file_data()
## Loads the data from the variable above into seperate variable used to complete the conn factory
my_file.load_file_data()
## Establishes connection
my_file.establish_connection()
## Get files from remote path
my_file.get_files()
