import cPickle as pickle
import os
import random
import nltk
from nltk import NaiveBayesClassifier
from nltk.corpus import brown
from nltk.tag.stanford import POSTagger
import time
from sklearn import neighbors
from sklearn.svm import SVC

__author__ = 'Luke'

news_sent = brown.sents(categories='news')
reviews_sent = brown.sents(categories='reviews')

print str(len(news_sent)) + ' ' + str(len(reviews_sent))

# tagger = TreeTagger(encoding='latin-1', language='english')
tagger = POSTagger('stanford-model.tagger', 'stanford-postagger.jar')

news_co_tr = int(0.9 * len(news_sent))
rev_co_tr = int(0.9 * len(reviews_sent))
brown_train = news_sent[:news_co_tr] + reviews_sent[:rev_co_tr]

news_co_te = int( len(news_sent))
rev_co_te = int( len(reviews_sent))
brown_test = news_sent[news_co_tr:news_co_te] + reviews_sent[rev_co_tr:rev_co_te]

train_target = []
for x in xrange(news_co_tr):
    train_target.append('news')

for x in xrange(rev_co_tr):
    train_target.append('rev')

test_target = []
for x in xrange(news_co_te - news_co_tr):
    test_target.append('news')
for x in xrange(rev_co_te - rev_co_tr):
    test_target.append('rev')

print str(len(test_target)) + " " + str(len(brown_test))
print str(len(train_target)) + " " + str(len(brown_train))
print test_target
print train_target

print brown_test
print len(brown_train)
print len(brown_test)



print extract_tags(tagger.tag(brown.sents(categories='news')[0]))

train_tagged_sents = tagger.batch_tag(brown_train)
training_set = [extract_tags(tagged_sent) for tagged_sent in train_tagged_sents]
test_tagged_sents = tagger.batch_tag(brown_test)
test_set = [extract_tags(tagged_sent) for tagged_sent in test_tagged_sents]

# pickle.dump(training_set, open("../../Data/Training/tagged-sents.obj", "wb"))

knn = neighbors.KNeighborsClassifier(algorithm='auto',
                                     leaf_size=30, n_neighbors=7)
knn.fit(training_set, train_target)
print knn.score(test_set, test_target)


knn = neighbors.KNeighborsClassifier(algorithm='auto',
                                     leaf_size=30, n_neighbors=5)
knn.fit(training_set, train_target)
print knn.score(test_set, test_target)


clf = SVC()
clf.fit(training_set, train_target)
print clf.score(test_set, test_target)

