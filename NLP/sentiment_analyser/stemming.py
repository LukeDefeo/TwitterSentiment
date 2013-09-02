__author__ = 'Luke'
from nltk import PorterStemmer
stemmer =  PorterStemmer()
print stemmer.stem('rushing')
print stemmer.stem_word('complications')
print stemmer.stem_word('complicated')
print stemmer.stem_word('awful')
print stemmer.stem_word('terrible')
print stemmer.stem_word('terribly')

print stemmer.stem_word('crazy')
print stemmer.stem_word('amazing')
print stemmer.stem_word('loving')
