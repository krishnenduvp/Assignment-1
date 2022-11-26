# DHCP Log Analyzer

## Table of Contents

**[Description](#description)**<br>
**[Functionalities](#functionalities)**<br>
**[Overview](#overview)**<br>
**[Unit Testing](#unit-testing)**<br>
**[To Do](#to-do)**<br>
**[Authors](#authors)**<br>

# Description

This is a log analysis tool that is used to collect, parse, and analyze the data written to DHCP log files. This script generates a csv file that contains a unique list of network devices that are connected to the system. The script reads the provided dhcpd log file and filters the line containing the message "DHCPACK," acknowledging that the IP address in question has been successfully leased to the client, and then filters out the mac address, ip address, hostname, and vendor name. In order to get the vendor name of the device, the script compares the MAC address with the OUI dictionary.

## Functionalities

| Script   |      Usage      | 
|----------| :---------------|
| create_directory.bat | Batch file to create project directories   | 
| create_directory.sh | Bash script to create project directories   | 
| check_file.py |  Confirm log path exists |
| open_file.py |  Reads file line by line   | 
| filter_dhcpd_log.py | To extract required details from log file| 
| get_mac_details.py | To get vendor details| 
| macaddress_dict.py |  Dictionary of MAC address |
| to_csv.py | To create required csv file | 
| pylint_testing.sh  | Bash script to perform pylint test| 
| test_dhcp_log_analyser.py | To perform unit testing on functions used  | 
  
## Overview

1. main.py

This acts as the point of execution for our "dhcp_log_analyser" Python project. It imports all the necessary modules from the "Source" directory required for proper functioning of the script. The main constant variables used here are DHCPD_LOG_PATH and OUTPUT_CSV_FILE. The user can specify the logpath in DHCPD_LOG_PATH and the csv filename that needs to be generated is mentioned in OUTPUT_CSV_FILE.

The script begins by importing check_file.py to confirm the dhcpd log path exists and is not an empty file. If the condition is met, it opens the dhcpd log file using the function open_file() in open_file.py. And then it imports filter_dhcpd_log.py to filter out the required values. filter_dhcpd_log.py uses get_mac_details.py to get the vendor details of the connected devices. Finally, it returns a list of tuples containing the MAC address, IP address, hostname, and vendor information. The result is fed to to_csv.py, which creates the final csv file nodes.csv.

2. check_file.py

This script imports the built-in Python modules os and sys. The main functionality of the script is to check the existence of the provided filepath and confirm whether the file is not an empty file. For this, the detect_path() and file_not_empty() functions are used, respectively. In both cases, if the condition is not met, the program exits using sys.exit(0).

3. open_file.py

The open_file() function is used to open an input file and read it. While performing the file operations here, most common exceptions are handled here using the try and except statements.

4. filter_dhcpd_log.py

The script filter_dhcpd_log.py reads the dhcpd log file, then extracts and provides important information about connected devices using regex operations. The main idea behind using regex operations is code reuseability, i.e., the same regex or functions can be used to filter out required details from other system log files too. The main regex patterns used here are :

```python
# Regex to filter only connected devices using "DHCPACK on" string
dhcp_pattern = re.compile('DHCPACK on')
# Regex to get IP address
ip_pattern = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
# Regex to get 6 pairs of alphanumberic string of ":xx:"
mac_pattern = re.compile(r'(?:[0-9a-fA-F]:?){12}')
# Regex to get string between brackets example : "(kali)"
hostname_pattern = re.compile('\((.*?)\)')
``` 

The function filter_log_file returns a list of tuples containing the MAC address, IP address, Hostname and Vendor information like below :

```python
[('c8:4b:d6:0a:77:2d', '192.168.5.168', 'A-76MRRL3', 'Dell Inc'), ('18:68:cb:45:1a:ae', '192.168.12.102', 'NO_HOSTNAME', 'Hangzhou Hikvision'), ('b8:27:eb:b4:81:6d', '192.168.5.172', 'kali', 'Raspberry Pi Foundation')]
``` 

5. get_mac_details.py

The script get_mac_details.py checks the mac address dictionary "./macaddress_dict" and provides the vendor details of a given mac address using the function get_mac_vendor. The function test_input_mac_address() is used to validate the user input when the script is executed as a standalone script, here an example of assert regex testing is showcased.

```python
def test_input_mac_address():
    """ To test that input value matches a standard mac address pattern"""
    mac_pattern = re.compile(r'(?:[0-9a-fA-F]:?){6}')
    assert re.match(mac_pattern, input_mac_address)
```

<b>Dependenices: macaddress_dict.py</b>

6. macaddress_dict.py

This file contains MAC address details of various manufactures required for this project like below:

```python
dell_manufacture = {
    "oui"  : ['c8:4b:d6','a4:4c:c8','c0:25:a5'],
    "vendor" : "Dell Inc",
    "company_address" : "One Dell Way Round Rock TX 78682 US"
}
``` 

7. to_csv.py

The script to_csv.py creates a csv file from the list provided. There is also the function unique_to_csv_file(), which writes only unique values to csv. This script can be run independently or from other programs. 

## Unit Testing

1. pylint_testing.sh

A bash script was developed to review Python scripts using the PyLint code analyzer. The script can be used to print detailed or short test results for single or multiple Python files. Sample output is shown below :

```bash
l00170964@l00170964:~/python$ ./pylint_testing.sh
Enter directory/file name to test code : Source/
Would you like print short(s|S) or detailed(d|D) result : s
Performing pylint test, please wait..
CODE : Source/macaddress_dict.py         RATING : 10.00/10
CODE : Source/open_file.py       RATING : 8.89/10
CODE : Source/to_csv.py          RATING : 8.33/10
CODE : Source/get_mac_details.py         RATING : 7.27/10
CODE : Source/filter_dhcpd_log.py        RATING : 5.37/10
CODE : Source/check_file.py      RATING : 8.89/10
l00170964@l00170964:~/python$
``` 
2. test_dhcp_log_analyser.py

In dhcp_log_analyser project, a subclass of unittest.TestCase called "TestDhcp" is created to test the common functions. The functions used here are test_detect_path,test_file_not_empty, test_get_mac_vendor, test_open_file and test_unique_to_csv_file.

```python
python -m unittest discover .
The file path ./dhcpd.log exists 
.The file ./dhcpd.log is not empty
...[('MAC ADDR', 'IP ADDR', 'HOSTNAME', 'VENDOR')]
.
----------------------------------------------------------------------
Ran 5 tests in 0.003s

OK
``` 

## To Do

The script "test_dhcp_log_analyser.py" used for unit testing the Python project only runs when called from within the Source directory rather than Tests/test_dhcp_log_analyser.py. From the Tests directory, need to find a solid approach to performing unit testing. Below is the error that is produced when calling from the Tests directory. A solution was discovered through research, but it was not feasible. It was to append the project's path to the PYTHONPATH environment variable.

```python
Error : ModuleNotFoundError: No module named 'check_file'
```

## Reusability

All the scripts written for this project were developed to run as standalone scripts or from other programs. Evident use of functions can be seen throughout the project.

## Authors

DHCP Log Analyzer tool was developed as a part of Infrastructure as Code module's assignment by Krishnendu VP.
