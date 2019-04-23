import sys
import re

usage = "usage: txt_to_dict.py [file]\n'file' must use '#' (pound sign) as delimiter, as:\nkey1#value1\nkey2#value2\n...\n"

# Print usage
args = sys.args()
if length(args) == 1:
    print usage
    exit()

# Read text file into Python dict
f = open(args[1],'rU')
