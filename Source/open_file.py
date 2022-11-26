'''
Script : open_file
Author : Krishnendu
Purpose : To open a file and read line by line
Usage : python open_file.py
Revision History :
Aplha Version : 02-Nov-2022
Tested : Windows-10-10.0.22621-SP0 with Python version 3.10.7
Notes : This script could also be executed independently and called from another script using
an import statement like the one outlined below:
from open_file import open_file
file_lines = open_file(file_location)
'''
# Import modules
# Functions
def open_file(file_location)->str:
    """To open a file, common exceptions are handled here"""
    try:
        with open(file_location) as file_handler:
            fstring = file_handler.readlines()
            return fstring
    except IOError as err:
        print(f"IOError was {err}")
    except EOFError as err:
        print(f"End of file error was {err}")
    except:
        print("General Error ..")
    return None
# Main program
# Condition to check if script is executed as a standalone script or not
if __name__ == '__main__':
    print("This module executes as a standalone script")
    # Input file location
    file_path = input("Enter path location : ")
    file_lines = open_file(file_path)
    print(file_lines)
else:
    pass
