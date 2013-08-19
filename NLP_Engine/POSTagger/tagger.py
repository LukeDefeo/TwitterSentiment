import nltk
import cPickle as pickle
__author__ = 'Luke'

nltk.BrillTagger
from nltk.tag.stanford import StanfordTagger



#get data


from nltk.corpus import brown
from nltk.tag import UnigramTagger
from nltk.tag.brill import SymmetricProximateTokensTemplate, ProximateTokensTemplate
from nltk.tag.brill import ProximateTagsRule, ProximateWordsRule, FastBrillTaggerTrainer

news_sent = brown.tagged_sents(categories='news')
reviews_sent = brown.tagged_sents(categories='reviews')

print str(len(news_sent)) + ' ' +  str(len(reviews_sent))
brown_train = news_sent[:int(0.9*len(news_sent))] + reviews_sent[:int(0.9*len(reviews_sent))]

brown_test = news_sent[int(0.9*len(news_sent)):] + reviews_sent[int(0.9*len(reviews_sent)):]

t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(brown_train, backoff=t0)
t2 = nltk.BigramTagger(brown_train, backoff=t1)
print t2.evaluate(brown_test)

print t2.tag(brown_train[0])

reviews_sent = brown.tagged_sents(categories='reviews')
reviews_sent_untagged = brown.sents(categories='reviews')
print reviews_sent[0]
print reviews_sent_untagged[0]

tagger = t2
pickle.dump(tagger, open("../../Data/Training/tagger.obj", "wb"))

print "done"


# unigram_tagger = UnigramTagger(brown_train)
# templates = [
#     SymmetricProximateTokensTemplate(ProximateTagsRule, (1, 1)),
#     SymmetricProximateTokensTemplate(ProximateTagsRule, (2, 2)),
#     SymmetricProximateTokensTemplate(ProximateTagsRule, (1, 2)),
#     SymmetricProximateTokensTemplate(ProximateTagsRule, (1, 3)),
#     SymmetricProximateTokensTemplate(ProximateWordsRule, (1, 1)),
#     SymmetricProximateTokensTemplate(ProximateWordsRule, (2, 2)),
#     SymmetricProximateTokensTemplate(ProximateWordsRule, (1, 2)),
#     SymmetricProximateTokensTemplate(ProximateWordsRule, (1, 3)),
#     ProximateTokensTemplate(ProximateTagsRule, (-1, -1), (1, 1)),
#     ProximateTokensTemplate(ProximateWordsRule, (-1, -1), (1, 1)),
# ]
# trainer = FastBrillTaggerTrainer(initial_tagger=unigram_tagger,
#                                  templates=templates, trace=3,
#                                  deterministic=True)
# brill_tagger = trainer.train(brown_train, max_rules=200)
#
# print brill_tagger.evaluate(brown_test)