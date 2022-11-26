'''
Script : get_mac_details
Author : Krishnendu
Purpose : To provide vendor information of given mac address
Usage : python get_mac_details.py
Revision History :
Aplha Version : 02-Nov-2022
Tested : Windows-10-10.0.22621-SP0 with Python version 3.10.7
Notes : Script get_mac_details.py check's the mac address dictionary "./macaddress_dict"
and provides the vendor details of a given mac address. This script could also be executed
independently and called from another script using an import statement like below :
from get_mac_details import get_mac_vendor as get_manufacturer
oui_mac = mac_list.__str__()[0:8]
manufacture = get_manufacturer(oui_mac)
oui_mac: To get 24-bit number from mac address that uniquely identifies a vendor or manufacturer
'''
# Import modules
import re
# Uncomment this import statement to run as standalone script
# import macaddress_dict as mac_info
# Uncomment this import statement to run from a external application/program
import Source.macaddress_dict as mac_info

# Functions
def get_mac_vendor(oui_mac):
    """To compare 24-bit number mac address with "macaddress_dict" dictionary """
    #Checks mac address for Dell machines
    if oui_mac in mac_info.dell_manufacture['oui']:
        manufacture = mac_info.dell_manufacture['vendor']
    elif oui_mac in mac_info.raspberry_manufacture['oui']:
        manufacture = mac_info.raspberry_manufacture['vendor']
    elif oui_mac in mac_info.hangzhou_manufacture['oui']:
        manufacture = mac_info.hangzhou_manufacture['vendor']
    elif oui_mac in mac_info.asrock_manufacture['oui']:
        manufacture = mac_info.asrock_manufacture['vendor']
    else:
        # If provided mac address is not found in dictionary
        manufacture = "NOT FOUND"
    return manufacture

def test_input_mac_address():
    """ To test that input value matches a standard mac address pattern"""
    mac_pattern = re.compile(r'(?:[0-9a-fA-F]:?){6}')
    assert re.match(mac_pattern, input_mac_address)

# Main program
# Condition to check if script is executed as a standalone script or not
if __name__ == '__main__':
    print("This module executes as a standalone script")
    input_mac_address = str(input("Enter the Mac address, example 18:68:cb : "))
    test_input_mac_address()
    print(f"MacAddress : {input_mac_address} Vendor : {get_mac_vendor(input_mac_address)}")
else:
    pass
    