import csv, os, re
with open('DOID.csv') as rcsvfile, open('DOID_dict.csv','w') as wcsvfile:  
    rcsvfile.seek(0)
    reader = csv.reader(rcsvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    writer = csv.writer(wcsvfile)
    for i in reader:
        subrows = syn_to_rows(i)
        for row in subrows:
            writer.writerow(row)

'''Convert a row with synonyms to multiple rows with same definition'''
def syn_to_rows(row):
    # [1] term [2] syn1|syn2|... [3] def
    rows = [(row[1],row[3])]
    syn_str = row[2]
    syns = re.subn(syn_str, )
    
