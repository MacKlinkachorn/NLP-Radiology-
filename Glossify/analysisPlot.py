import pickle
import os
import numpy as np
import sys
import re
from xml_to_text import xml_to_dict, join_as_str
from lex_to_dict import to_dict
import pdb
import matplotlib.pyplot as plt


freq  = pickle.load(open("wordfreq.pkl", "rb"))
words = freq.keys()
frequency = freq.values()
index = np.arange(len(words))
plt.bar(index, frequency)
plt.xlabel('words', fontsize=5)
plt.ylabel('frequency', fontsize=5)
plt.xticks(index, words, fontsize=5, rotation=30)
plt.title('occurence of each words')
plt.savefig('wordFrequency.png')
