# Small, ad-hoc program to convert reports in 'ecgen' folder from xml to txt

# Import lxml if you have it, otherwise xml
try:
    from lxml import etree
except ImportError:
    import xml.etree.ElementTree as etree

import sys
import os
import errno


# See lxml documentation for more info
def xml_to_dict(xmlfile):
    tree = etree.parse(xmlfile)
    root = tree.getroot()
    # find all sections of the xml doc labeled 'AbstractText'
    abstr = root.findall(".//AbstractText")

    dict_list = []  # this will hold one dict per abstract section
    for section in abstr:
        s = section.attrib  # dict containing label name
        if not section.text:
            s['Text'] = ''  # catch null text pointer
        else:
            s['Text'] = section.text  # add the text of the section
        dict_list.append(s)

    return dict_list


def join_as_str(dict_list):
    out = ''
    for d in dict_list:
        out += '\n' + d['Label'] + '\n' + d['Text'] + '\n'
    return out

def xml_to_str(xmlfile):
    dicts = xml_to_dict(xmlfile)
    return join_as_str(dicts)

def main():
    args = sys.argv[1:]

    # usage
    if not args:
        print('usage: xml_to_text.py [-d dirpath] file1.xml [file2.xml ...]\n')
        print('Use the -d flag to specify output directory. Default is current directory.')
    
    # check for -d flag
    if args[0] == '-d':
        outdir = args[1]
        if outdir[-1] != '/':
            outdir += '/'
        args = args[2:]
    else:
        outdir = sys.path[0]
    
    
    # convert xml reports to text
    for arg in args:
        if not is_xml(arg):
#           print('Please input .xml reports only!'; exit(1))
            print('Please input .xml reports only!')

        text = xml_to_str(arg)
        filename = arg[:-4]
        outpath = outdir + filename + '.txt'
        
        filename = outdir + '/' + ".txt"
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise





if __name__ == '__main__':
    main()
