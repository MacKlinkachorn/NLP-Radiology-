import spacy
from spacy.tokenizer import Tokenizer
from spacy.lang.en import English

import os
#for text parsing 
import xml_to_text_p3 as parser


def build_tokenizable_data(nlp, report_dir):
	"""
	Creates a list of strings from the main bodies of text in .xml files passed in
	docs - a list of strings of the main body of reports

	"""

	#Loads data from docs into a texts string:
	docs = []
	for doc in os.listdir(report_dir):
		try:
			main_report = parser.xml_to_str(report_dir+doc)
			main_report = main_report
			docs.append(main_report)
		except:
			pass

	return docs
	

def load_data(report_dir):
	"""
	Loads radiology reports into a 'Spacy' pipeline, including processing.
	"""

	#Load the English model
	nlp = spacy.load("en_core_web_sm")

	#Load up radiology reports into a list of strings
	docs = build_tokenizable_data(nlp, report_dir)

	#Begins first processing text data by tokens
	for text in docs:
		doc = nlp(text)
		for token in doc:
			print(token.text, token.lemma_, token.has_vector, token.vector_norm)

	##NEXT STEP


if __name__ == '__main__':
	import sys
	report_dir = sys.argv[1]
	load_data(report_dir)

	#Default default dir: "../Glossify/ecgen-radiology/"



