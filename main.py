import spacy
from tools import render_dependency_tree, extract_information
nlp = spacy.load("en_core_web_sm")

sentences = ["On Friday, board members meet with senior managers " +
             "to discuss future development of the company.",
             "Boris Johnson met with the Queen last week.",
             "Donald Trump meets the Queen at Buckingham Palace.",
             "The two leaders also posed for photographs and " +
             "the President talked to reporters."]

for sent in sentences:
    print(f"\nSentence = {sent}")
    doc = nlp(sent)
    extract_information(doc)
    render_dependency_tree(doc)
