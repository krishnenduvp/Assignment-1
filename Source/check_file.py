'''
Script : check_file
Author : Krishnendu
Purpose : To check if provided file exists and is not a empty file
Usage : python check_file.py
Revision History :
Aplha Version : 02-Nov-2022
Tested : Windows-10-10.0.22621-SP0 with Python version 3.10.7
Notes : Contains two functions to check file path and to check if file is empty or not.
This script could also be executed independently and called from another script using
an import statement like the one outlined below. :
from check_file import detect_path as verify_file_path
from check_file import file_not_empty as verify_file_notempty
verify_file_path(file_location)
verify_file_notempty(file_location)
'''
# Import modules
import os
import sys
# Functions
def detect_path(file_location)->str:
    """To check if provided file path exists or not"""
    if os.path.exists(file_location):
        print(f"The file path {file_location} exists ")
        return True
    else:
        print(f"The file path {file_location} not found, program exiting !!!")
        sys.exit(0)

def file_not_empty(file_location)->str:
    """To check if provided file path is empty or not"""
    if os.stat(file_location).st_size == 0:
        print("The file {file_location} is empty, program exiting !!!")
        sys.exit(0)
    else:
        print(f"The file {file_location} is not empty")
        return True

# Main program
# Condition to check if script is executed as a standalone script or not
if __name__ == '__main__':
    print("This module executes as a standalone script")
    file_location = input("Enter path location : ")
    detect_path(file_location)
    file_not_empty(file_location)
else:
    pass
