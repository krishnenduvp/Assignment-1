'''
Script : test_dhcp_log_analyser
Author : Krishnendu
Purpose : To unit test functions used in dhcp_log_analyser 
Usage : python -m unittest test_dhcp_log_analyser.py
Revision History :
Aplha Version : 17-Nov-2022
Tested : Windows-10-10.0.22621-SP0 with Python version 3.10.7
Notes : This script needs to be run from project's Source directory, if module not found
error is raised please uncomment the import line in respective python script.
'''
# Import modules
import unittest
import os
from check_file import detect_path,file_not_empty
from get_mac_details import get_mac_vendor
from open_file import open_file
from to_csv import unique_to_csv_file

class TestDhcp(unittest.TestCase):
    """Basic test class"""
    def test_detect_path(self):
        """The actual test. Any method which starts with ``test_`` will considered as a test case."""
        call_to_test = detect_path("./dhcpd.log")
        assert call_to_test == True

    def test_file_not_empty(self):
        """Test to check whether log file is empty or not"""
        file_not_empty_result = file_not_empty("./dhcpd.log")
        assert file_not_empty_result == True

    def test_get_mac_vendor(self):
        """Test method to check the vendor is returned correctly for a give OUI number"""
        get_mac_vendor_result = get_mac_vendor("a4:4c:c8")
        self.assertEqual(get_mac_vendor_result, "Dell Inc")
    
    def test_open_file(self):
        """Test method to check if file can be opened and read"""
        open_file_result = open_file("./dhcpd.log")
        assert open_file_result != None

    def test_unique_to_csv_file(self):
        """Test method that checks whether a csv file is created as expected"""
        OUTPUT_CSV_FILE = "test_nodes.csv"
        row_header = [('MAC ADDR', 'IP ADDR', 'HOSTNAME', 'VENDOR')]
        unique_to_csv_file_result = unique_to_csv_file(OUTPUT_CSV_FILE, row_header)
        assert os.path.exists(OUTPUT_CSV_FILE) == True

if __name__ == '__main__':
    unittest.main()