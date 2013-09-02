import os
from nltk.tag.stanford import POSTagger

__author__ = 'Luke'

pos_tagger = POSTagger(os.path.join(os.path.dirname(__file__), 'stanford-model.tagger'),
                       os.path.join(os.path.dirname(__file__), 'stanford-postagger.jar'), encoding='utf8')

print pos_tagger.tag('The antenna on my Iphone is crap, I hate having no signal'.split())
print pos_tagger.tag('Apple losing billions due to fault with new iphone'.split())
print pos_tagger.tag('i like the Iphone'.split())
