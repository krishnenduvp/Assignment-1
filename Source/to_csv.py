'''
Script : to_csv
Author : Krishnendu
Purpose : To create a csv file from list of tuples
Usage : python to_csv.py
Revision History :
Aplha Version : 02-Nov-2022
Tested : Windows-10-10.0.22621-SP0 with Python version 3.10.7
Notes : Script to_csv.py creates a csv file from the list provided. Also
contains a function to write only unique values to csv. This script could
also be executed independently and called from another script using an import statement like below :
from to_csv import to_csv_file as create_csv
create_csv(output_csv_filename, rowlist)
from to_csv import unique_to_csv_file as unique_csv
unique_csv(output_csv_filename, rowlist)
'''
# Import modules
import csv
# Functions
def to_csv_file(filename:str(),rowlist):
    """To write csv file with the list provided"""
    # name should be filename.csv
    with open(filename, 'w') as outcsv:
        writer = csv.writer(outcsv, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        # To calculate the coloums
        item_length = len(rowlist[0])
        for item in rowlist:
            # Write to row
            writer.writerow([item[count] for count in range(item_length)])

def unique_to_csv_file(filename:str(),rowlist):
    """To find unique values in list and write to csv file"""
    unique_list = []
    for item in rowlist:
        if item not in unique_list:
            unique_list.append(item)
    rowlist = unique_list
    print(rowlist)
    to_csv_file(filename, rowlist)
# Main program
# Condition to check if script is executed as a standalone script or not
if __name__ == '__main__':
    print("This module executes as a standalone script")
    print("This script will create a csv file from list")
    # Dummy row header and data to create a sample csv file "student.csv"
    OUTPUT_CSV_FILENAME = "student.csv"
    row_header = [('Name', 'Age', 'Course', 'Country')]
    each_row = [('Krish', '24', 'Cloud', 'India'), ('Stefan', '22', 'Devops', 'Austria')]
    rowlist = row_header + each_row
    to_csv_file(OUTPUT_CSV_FILENAME, rowlist)
else:
    pass
    