from nltk.corpus import brown
from nltk.tag.stanford import POSTagger

__author__ = 'Luke'

tagger = POSTagger('stanford-model.tagger', 'stanford-postagger.jar')

# print tagger.tag("what is the airspeed of an unlaiden swallow?".split())

l = ["what is the airspeed of an unlaiden swallow?".split(), "Call me Luke.".split()]
print l
print tagger.batch_tag(l)

reviews_sent_untagged = brown.sents(categories='reviews')[0:20] + brown.sents(categories='news')[0:20]

print tagger.batch_tag(reviews_sent_untagged)

