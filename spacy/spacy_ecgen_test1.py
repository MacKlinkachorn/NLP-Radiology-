import spacy
from spacy.tokenizer import Tokenizer
from spacy.lang.en import English
from spacy.pipeline import Tagger
from spacy.pipeline import TextCategorizer
import os
import pickle as pkl
# for text parsing
import xml_to_text_p3 as parser
import re # regular expressions
import urllib  # the lib that handles the url stuff

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

# not sure how to iterate functions but could be used in the future
# def helper(token, keys, f, dicts):
#     alltokens = {}
#     alltokens[token.text] = []
#     for i in range(len(dicts)):
#         if keys[i] not in dicts[i]:
#             dicts[i][keys[i]] = [token.f[i]]
#         else:
#             dicts[i][keys[i]].append(token.f[i])
#         alltokens[token.text].append(dicts[i])
#     return alltokens

def build_doc_dicts(doc, report_dir):
    #Total dictionary of tokens first (if we need all tokens for example), and counter for file name
    alltokens = {}

    #strings for all dictionaries, 7 so far
    HASVECTOR = str("has vector")
    VECTORNORM = str("vector norm")
    ISOOV = str("is oov")
    LEMMA = str("lemma")
    TAGS = str("tags")
    SHAPES = str("shapes")
    DEPS = str("deps")
    # strings = [HASVECTOR, VECTORNORM, ISOOV, LEMMA, TAGS, SHAPES, DEPS]
    # functions = [has_vector, vector_norm, is_oov, lemma, tag, shape, dep_]

    # multiple dictionaries for each feature to search for, dictionary in dictionary (Solar or Lucian indexing?)
    hasvector = {}
    vectornorm = {}
    isoov = {}
    lemma = {}
    tags = {}
    shapes = {}
    deps = {}
    # labels = {}
    # dicts = [hasvector, vectornorm, isoov, lemma, tags, shapes, deps]
    # iterature through tokens in a document and generate subdictionaries
    for textfilename in os.listdir(report_dir):
        for token in doc:
            if token.text not in alltokens:
                alltokens[token.text] = []
                # alltokens.append(helper(alltokens, token, strings, functions, dicts))
                if HASVECTOR not in hasvector:
                    hasvector[HASVECTOR] = [token.has_vector]
                else:
                    hasvector[HASVECTOR].append(token.has_vector)
                alltokens[token.text].append(hasvector)
                if VECTORNORM not in vectornorm:
                    vectornorm[VECTORNORM] = [token.vector_norm]
                else:
                    vectornorm[VECTORNORM].append(token.vector_norm)
                alltokens[token.text].append(vectornorm)
                if ISOOV not in isoov:
                    isoov[ISOOV] = [token.is_oov]
                else:
                    isoov[ISOOV].append(token.is_oov)
                alltokens[token.text].append(isoov)
                if LEMMA not in lemma:
                    lemma[LEMMA] = [token.lemma_]
                else:
                    lemma[LEMMA].append(token.lemma_)
                alltokens[token.text].append(lemma)
                if TAGS not in tags:
                    tags[TAGS] = [token.tag_]
                else:
                    tags[TAGS].append(token.tag_)
                alltokens[token.text].append(tags)
                if SHAPES not in shapes:
                    shapes[SHAPES] = [token.shape_]
                else:
                    shapes[SHAPES].append(token.shape_)
                alltokens[token.text].append(shapes)
                if DEPS not in deps:
                    deps[DEPS] = [token.dep_]
                else:
                    deps[DEPS].append(token.dep_)
                alltokens[token.text].append(deps)
            else:
                # alltokens.append(helper(alltokens, token, strings, functions, dicts))
                if HASVECTOR not in hasvector:
                    hasvector[HASVECTOR] = [token.has_vector]
                else:
                    hasvector[HASVECTOR].append(token.has_vector)
                alltokens[token.text].append(hasvector)
                if VECTORNORM not in vectornorm:
                    vectornorm[VECTORNORM] = [token.vector_norm]
                else:
                    vectornorm[VECTORNORM].append(token.vector_norm)
                alltokens[token.text].append(vectornorm)
                if ISOOV not in isoov:
                    isoov[ISOOV] = [token.is_oov]
                else:
                    isoov[ISOOV].append(token.is_oov)
                alltokens[token.text].append(isoov)
                if LEMMA not in lemma:
                    lemma[LEMMA] = [token.lemma_]
                else:
                    lemma[LEMMA].append(token.lemma_)
                alltokens[token.text].append(lemma)
                if TAGS not in tags:
                    tags[TAGS] = [token.tag_]
                else:
                    tags[TAGS].append(token.tag_)
                alltokens[token.text].append(tags)
                if SHAPES not in shapes:
                    shapes[SHAPES] = [token.shape_]
                else:
                    shapes[SHAPES].append(token.shape_)
                alltokens[token.text].append(shapes)
                if DEPS not in deps:
                    deps[DEPS] = [token.dep_]
                else:
                    deps[DEPS].append(token.dep_)
                alltokens[token.text].append(deps)
        f = open(str(textfilename) + ".pkl", "wb")
        pkl.dump(alltokens, f)
        f.close()
    # print(alltokens)
    # print(isoov)
    # print(lemma)
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

    #Begins first processing text data by tokens
    for text in docs:
        doc = nlp(text)
        build_doc_dicts(doc, report_dir)


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
    # parse_lexicon()
    # for sameer: /Users/sameersundrani/NLP-Radiology-/ecgen-radiology
    #Default default dir: "../Glossify/ecgen-radiology/"



