# This script perform an analysis on the text data 

"""
TODO:


"""
import pickle
import os
import numpy as np 
import sys
import re
from xml_to_text import xml_to_dict, join_as_str
from lex_to_dict import to_dict
import pdb
import matplotlib.pyplot as plt


def main():
    file_list = [f for f in os.listdir('./ecgen-radiology') if os.path.isfile(os.path.join('./ecgen-radiology', f))]
    gloss_files = ['UPenn_glossary.csv', 'UMich_glossary.json']
    gloss = combine(gloss_files) #dict
    allwordinGloss = []
    wordinDoc = []
    for filename in file_list:
    	text = xml_to_dict("ecgen-radiology/" + filename) # list of dicts, one per section
        text = join_as_str(text) # string
        out = annotate(text, gloss)
        numword = len(out)
        wordinDoc.append(numword)
        allwordinGloss += out
    freq = {} 
    for items in allwordinGloss: 
        freq[items] = allwordinGloss.count(items)
    f = open("wordfreq.pkl","wb")
    pickle.dump(freq,f)
    f.close()
    words = freq.keys()
    frequency = freq.values()
    plt.ion()
    # this is for plotting purpose
    index = np.arange(len(words))
    plt.barh(index, frequency)
    plt.xlabel('words', fontsize=5)
    plt.ylabel('frequency', fontsize=5)
    plt.xticks(index, words, fontsize=5, rotation=30)
    plt.title('occurence of each words')
    plt.savefig('wordFrequency.png')
    plt.show()
    plt.ion()
    index = np.arange(len(file_list))
    plt.bar(index, wordinDoc)
    plt.xlabel('documents', fontsize=5)
    plt.ylabel('words in documents', fontsize=5)
    plt.xticks(index, file_list, fontsize=5, rotation=30)
    plt.title('number of word in each documents')
    plt.savefig("wordinDocuments.png")
    plt.show()









def annotate(text, gloss):
	# For each word in the glossary, look for matches in the text
    found = [] # will hold found terms and definitions
    num = 1
    for word in gloss.keys():
        # For each match, annotate it with a number
        (text, n) = re.subn(r'('+ word +')',r'\1('+ str(num) +')',text)
        # If there's a match, add the term and defitition to 'found'
        if (n > 0):
            index = text.index(word)
            found.append(word)
            num += 1
    # Sort words by the order they appear in text
    found.sort(cmp=lambda x,y: cmp(x[1],y[1]))
    return found

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



# boilerplate for terminal compatability
if __name__ == '__main__':
    main()
