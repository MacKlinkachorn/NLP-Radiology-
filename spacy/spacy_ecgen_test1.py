import spacy
from spacy.tokenizer import Tokenizer
from spacy.lang.en import English

import os
#for text parsing 
import xml_to_text_p3 as parser


def build_tokenizer(nlp, report_dir):
	"""
	Creates a tokenizer from the main bodies of text in .xml files passed in
	"""
	#tokenizer = Tokenizer(nlp.vocab)
	#print(tokenizer)

	#Loads data from docs into a texts string:
	docs = []
	for doc in os.listdir(report_dir):
		try:
			main_report = parser.xml_to_str(report_dir+doc)
			docs.append(main_report)
		except:
			pass

	print(docs)
		
	#for doc in Tokenizer.pipe(docs):
	#	print(doc)
	#	for token in doc:
	#		print(token.text, token.lemma_)


	#rad_tokens = [token.text for token in nlp(doc) for doc in texts]
	#print(rad_tokens)



def load_data(report_dir):
	"""
	Loads radiology reports into a 'Spacy' pipeline, including processing.
	"""


	#Load the English model
	nlp = spacy.load("en_core_web_sm")

	build_tokenizer(nlp, report_dir)


if __name__ == '__main__':
	import sys
	report_dir = sys.argv[1]
	load_data(report_dir)

	#Default default dir: "../Glossify/ecgen-radiology/"



