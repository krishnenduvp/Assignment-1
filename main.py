'''
Script : dhcp_log_analyzer|main.py
Author : Krishnendu
Purpose : To analyze dhcp logs and filter out unique connections to a csv file
Usage : python main.py
Revision History :
Aplha Version : 02-Nov-2022
Tested : Windows-10-10.0.22621-SP0 with Python version 3.10.7
Notes : Script will create a nodes.csv file with mac address,ip,hostname and manufacturer name
'''
# Import modules
from Source.check_file import detect_path as verify_file_path
from Source.check_file import file_not_empty as verify_file_notempty
from Source.open_file import open_file as open_dhcpd_log
from Source.filter_dhcpd_log import filter_log_file
from Source.to_csv import unique_to_csv_file as unique_list_to_csv

# Variables
DHCPD_LOG_PATH = './dhcpd.log' # Path to dhcpd log file
OUTPUT_CSV_FILE = "nodes.csv"
row_header = [('MAC ADDR', 'IP ADDR', 'HOSTNAME', 'VENDOR')] # Row header for nodes.csv

# Verify log path exists and is not empty
verify_file_path(DHCPD_LOG_PATH)
verify_file_notempty(DHCPD_LOG_PATH)
# Open log file and read lines
log_lines = open_dhcpd_log(DHCPD_LOG_PATH)
# Extract required information from log file
each_row = filter_log_file(log_lines)
# Combine row header and required data from each line of log file
rowlist = row_header + each_row
# Creates "nodes.csv" file with required data i.e, unique connections
unique_list_to_csv(OUTPUT_CSV_FILE, rowlist)
