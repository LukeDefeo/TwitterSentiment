import os
from nltk.tag.stanford import POSTagger

__author__ = 'Luke'

pos_tagger = POSTagger(os.path.join(os.path.dirname(__file__), 'stanford-model.tagger'),
                       os.path.join(os.path.dirname(__file__), 'stanford-postagger.jar'), encoding='utf8')


print pos_tagger.tag('I like the product'.split())

print pos_tagger.tag('This product is pretty bad, like every other one they made'.split())
print pos_tagger.tag('Apple losing billions due to fault with new iphone'.split())
print pos_tagger.tag('ahhhh The antenna on my Iphone is rubbish, I hate having no signal'.split())
