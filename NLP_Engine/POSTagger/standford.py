# coding=utf-8
from nltk.corpus import brown
from nltk.tag.stanford import POSTagger

__author__ = 'Luke'

tagger = POSTagger('stanford-model.tagger', 'stanford-postagger.jar')

# print tagger.tag("what is the airspeed of an unlaiden swallow?".split())

l = ["what is the airspeed of an unlaiden swallow?".split(), "Call me Luke."]
print l
print tagger.batch_tag(l)



s= 'ok α'
u = u'ok α'
def whatisthis(s):
    if isinstance(s, str):
        print "ordinary string" + s
    elif isinstance(s, unicode):
        print "unicode string" + s
    else:
        print "not a string"


whatisthis(s)
whatisthis(u)
print tagger.tag(s)
print tagger.tag(u.encode('utf8'))
whatisthis(u.encode('utf8'))
whatisthis(unicode(s,'utf8'))
print