from lxml import etree
import sys

# See lxml documentation for more info
def xml_to_dict(xmlfile):
    tree = etree.parse(xmlfile)
    root = tree.getroot()
    # find all sections of the xml doc labeled 'AbstractText'
    abstr = root.findall(".//AbstractText")

    dict_list = [] # this will hold one dict per abstract section
    for section in abstr:
        s = section.attrib # dict containing label name
        s['Text'] = section.text # add the text of the section
        dict_list.append(s)
    return dict_list


def main():
    args = sys.argv[1:]
    for arg in args:
        print xml_to_dict(arg)

if __name__ == '__main__':
    main()

