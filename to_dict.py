import sys
import re

# Read file into Python dict
def to_dict(filename):
    # handle CSV and JSON separately    
    extension = filename[-4:]
    if extension == '.json':
        import json
        with open(filename, 'rUb') as jsonfile:
            data = json.loads(jsonfile.read())
            return data

    else:
        import csv
        ### 'with...as' syntax closes the file as soon as execution leaves indented scope.
        ### More on CSV in Python:
        ### https://docs.python.org/3.4/library/csv.html
        ### https://docs.python.org/2/library/csv.html
        with open(filename,'rUb') as csvfile:
            dialect = csv.Sniffer().sniff(csvfile.read(1024))
            csvfile.seek(0)
            reader = csv.reader(csvfile, dialect)
            gloss = {} # new dictionary
            for row in reader:
                gloss[row[0]] = row[1]
            return gloss
    


def main():
    
    # Print usage
    args = sys.argv[1:]
    if not args:
        print "usage: txt_to_dict.py [file]"
        sys.exit(1)
    
    for filename in args:
        print to_dict(filename)


# Boilerplate for CLI
if __name__ == '__main__':
  main()

