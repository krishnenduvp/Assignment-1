'''
Script : filter_dhcpd_log
Author : Krishnendu
Purpose : To provide vendor information of given mac address
Usage : python filter_dhcpd_log.py
Revision History :
Aplha Version : 02-Nov-2022
Tested : Windows-10-10.0.22621-SP0 with Python version 3.10.7
Dependencies : get_mac_details.py
Notes : Script filter_dhcpd_log.py reads dhcpd log file, then extracts and provides important
information of connected devices using regex operations. This script could also be executed
independently and called from another script using an import statement like below :
from filter_dhcpd_log import filter_log_file,check_hostname,check_ip,check_mac_address
output = filter_log_file(log_lines)
The script has dependencies in get_mac_details.py
'''
# Import modules
import re # for regex opertions
# Uncomment this import statement to run as standalone script, also in get_mac_details.py
# from open_file import open_file as open_dhcpd_log
# from get_mac_details import get_mac_vendor as get_manufacturer
# Uncomment this import statement to run from a external application/program
from Source.open_file import open_file as open_dhcpd_log
from Source.get_mac_details import get_mac_vendor as get_manufacturer
# Functions
def check_hostname(search_hostname):
    """To check hostnaame is avaiable in the line read else marks it as "NO_HOSTNAME"""
    if search_hostname:
        hostname_result = search_hostname.group(1)
    else:
        hostname_result = "NO_HOSTNAME"
    return hostname_result

def check_ip(search_ip_addr):
    """To check IP address is avaiable in the line read else marks it as "NO_IPADDR"""
    if search_ip_addr:
        ip_addr_result = search_ip_addr.group()
    else:
        ip_addr_result = "NO_IPADDR"
    return ip_addr_result

def check_mac_address(search_mac_address):
    """To check mac address is avaiable in the line read else marks it as "NO_MACADDR"""
    if search_mac_address:
        mac_address_result = search_mac_address.group()
    else:
        mac_address_result = "NO_MACADDR"
    return mac_address_result

def filter_log_file(log_lines):
    """To filter out required ip,mac address,hostname using regex module"""
    for line in log_lines:
        line = line.rstrip() # To remove any trailing characters
        # Proceed if line contains DHCPACK string
        if re.search(dhcp_pattern, line):
            # Returns a Match object if there is a match anywhere in the string
            search_ip_addr = re.search(ip_pattern, line)
            search_mac_address = re.search(mac_pattern, line)
            search_hostname = re.search(hostname_pattern, line)
            # Checks if match object is found
            hostname_result = check_hostname(search_hostname)
            ip_addr_result = check_ip(search_ip_addr)
            mac_result = check_mac_address(search_mac_address)
            # To append the filtered output to respective list
            ip_list.append(ip_addr_result)
            mac_list.append(mac_result)
            hostname_list.append(hostname_result)
    # loop to slice 24bit OUI from mac address list
    len_of_list = len(mac_list)
    for i in range(len_of_list):
        oui_mac = mac_list[i].__str__()[0:8]
        # Compare and provide the manufacturer name of mac address
        manufacture = get_manufacturer(oui_mac)
        oui_mac_list.append(manufacture)
    # To store all list together in a understandable format
    dhcp_list = list(zip(mac_list,ip_list,hostname_list,oui_mac_list))
    return dhcp_list

# Variables
# Regex search pattern
# Regex to filter only connected devices using "DHCPACK on" string
dhcp_pattern = re.compile('DHCPACK on')
# Regex to get IP address
ip_pattern = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
# Regex to get 6 pairs of alphanumberic string of ":xx:"
mac_pattern = re.compile(r'(?:[0-9a-fA-F]:?){12}')
# Regex to get string between brackets example : "(kali)"
hostname_pattern = re.compile('\((.*?)\)')
# Define empty lists
ip_list = []
mac_list = []
hostname_list = []
oui_mac_list = []
to_csv_list = []
# Main program
# Condition to check if script is executed as a standalone script or not
if __name__ == '__main__':
    print("This module executes as a standalone script")
    DHCPD_LOG_PATH = 'C:\My Works\ATU\IaC\Assignment\dhcpd.log'
    # Open log file
    dhcp_log_lines = open_dhcpd_log(DHCPD_LOG_PATH)
    # Filter the dhcpd log
    dhcp_final_list = filter_log_file(dhcp_log_lines)
    print(dhcp_final_list)
else:
    pass
    