# Given a .txt file or an XML document like those in 'ecgen-radiology', 
# creates an annotated version with a glossary in a *.txt file.

import sys
import re
from xml_to_dict import xml_to_dict
from gloss_to_dict import to_dict
import pdb



# Annotate free text. 
def annotate(text, gloss):
    # For each word in the glossary, look for matches in the text
    found = [] # will hold found terms and definitions
    num = 1
    for word in gloss.keys():
        # For each match, annotate it with a number
        (text, n) = re.subn(r'('+ word +')',r'\1('+ str(num) +')',text)
        # If there's a match, add the term and defitition to 'found'
        if (n > 0):
            found.append((word,gloss[word]))
            num += 1
    # Print custom glossary below text
    out = text
    out += '\n' + '='*30 + '\n'
    for i in range(len(found)):
        out += '('+ str(i+1) +') '+ found[i][0] +': '+ found[i][1] +'\n'
    # Return annotated text as string
    return out

# Combine glossary files into a dict
def combine(file_list):
    # Convert each file type to a dict
    dicts = []
    for filename in file_list:
        dicts.append(to_dict(filename))

    # Combine dicts
    out = {}
    for d in dicts:
        out.update(d)
    return out

def join_as_str(dict_list):
    out = ''
    for d in dict_list:
        out += '\n' + d['Label'] + '\n' + d['Text'] + '\n'
    return out

# Returns whether the filename ends in '.xml'
def is_xml(filename):
    return filename[-4:].lower() == '.xml'


def main():
    # Make a list of command line arguments, omitting the [0] element, which is the name of this Python script.
    args = sys.argv[1:]
    
    # print usage if no args
    if not args:
        print 'usage: python glossary.py file [file ...]'
        #print 'usage: python glossary.py [-l lex.json] file [file ...]\nUse the -l option to use a custom lexicon (must be JSON).'
        sys.exit(1)
        
    # Combine glossary files into a dict
    gloss_files = ['UPenn_glossary.csv', 'UMich_glossary.json']
    #gloss_files.append(other_gloss_files)
    gloss = combine(gloss_files) #dict
    
    # Annotate each file with a glossary.
    for filename in args:
        text = xml_to_dict(filename) # list of dicts, one per section
        text = join_as_str(text) # string
        # annotate text using glossary
        out = annotate(text, gloss)

        # write glossary to a file 
        outf = open(filename + '.summary.txt', 'w')
        outf.write(text + '\n')
        outf.close()
        print out



# boilerplate for terminal compatability
if __name__ == '__main__':
    main()

