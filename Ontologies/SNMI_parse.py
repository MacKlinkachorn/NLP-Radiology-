import csv, os, pdb
with open('SNMI.csv') as rcsvfile, open('SNMI_dict.csv','w') as wcsvfile:  
    rcsvfile.seek(0)
    reader = csv.reader(rcsvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    writer = csv.writer(wcsvfile)
    for i in reader:
        writer.writerow([i[1],i[2]])
