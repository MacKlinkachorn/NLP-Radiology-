import spacy
from spacy.tokenizer import Tokenizer
from spacy.lang.en import English
from spacy.pipeline import Tagger
from spacy.pipeline import TextCategorizer
import os
import pickle as pkl
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
	nlp = spacy.load("en_core_web_lg")

	#Load up radiology reports into a list of strings
	docs = build_tokenizable_data(nlp, report_dir)

	docs_pipe = nlp.pipe(docs)

	with open("out.pkl", "wb") as f:
		pkl.dump(list(docs), f)

	#Begins first processing text data by tokenss
	#for text in docs:
	#	doc = nlp(text)
	#my_model = nlp.to_disk("Users/ianwoodward/Documents/GitRepos/NLP-Radiolgy-/spacy/spacy_out")
	#	data = pickle.dumps(doc)
		
		#for token in doc:
		#	print(token.text, token.similarity(doc))
		#	print(token.text, token.has_vector, token.vector_norm, token.is_oov)
		#	print(token.text, token.lemma_, token.tag_)
		#	print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
         #   token.shape_, token.is_alpha, token.is_stop)
         
		#Named entity recognition
		#for ent in doc.ents:
		#	print(ent.text, ent.start_char, ent.end_char, ent.label_)



if __name__ == '__main__':
	import sys
	report_dir = sys.argv[1]
	load_data(report_dir)

	#Default default dir: "../Glossify/ecgen-radiology/"



