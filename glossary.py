# Given a .txt file or an XML document like those in 'ecgen-radiology', 
# creates an annotated version with a glossary in a *.txt file.

# command line I/O utilities
import sys
# regular expression package
import re

# extracts the 'FINDINGS' field from an XML rad report
def extract(filename):
    f = open(filename, 'rU')
    xml = f.read()


# Returns whether the filename ends in '.xml'
def is_xml(filename):
#    print filename[-4:]
    return filename[-4:].lower == '.xml'

def main():
    # Make a list of command line arguments, omitting the [0] element
    # which is the Python script itself.
    args = sys.argv[1:]
    
    # print usage if no args
    if not args:
        print 'usage: file [file ...]'
        sys.exit(1)

    for filename in args:
        # extract text to be annotated from XML or .txt
        if is_xml(filename):
            pass
            text = extract_findings(filename)
        else:

            f = open(filename, 'rU')
            text = f.read()
        
        # create annotated glossary
        gloss = annotate(text)
        # write glossary to a file 
        if gloss:
            outf = open(filename + '.summary', 'w')
            outf.write(text + '\n')
            outf.close()

# boilerplate for terminal compatability
if __name__ == '__main__':
    main()

