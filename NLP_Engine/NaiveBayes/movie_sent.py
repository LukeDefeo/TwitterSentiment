__author__ = 'Luke'

import nltk
import random
from nltk import NaiveBayesClassifier
from nltk.corpus import names

from nltk.corpus import movie_reviews



#Get data
reviews = [(movie_reviews.words(fileid), category)
           for category in movie_reviews.categories()
           for fileid in movie_reviews.fileids(category)]

random.shuffle(reviews)
a = dict()
all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
common_words = all_words.keys() [:2000]


def doc_features(doc):
    doc_words = set(doc)
    features = {}
    for word in common_words:
        features["contains(%s)" % word] = (word in doc_words)

    return features

#generate feature set tuples, dict of features and catagory
feature_set = [(doc_features(doc), cat) for (doc, cat) in reviews]

cut_off = int(0.8 * len(feature_set))
train_set = feature_set[:cut_off]
test_set = feature_set[cut_off:]
classifier = NaiveBayesClassifier.train(train_set)

print ""


print nltk.classify.accuracy(classifier,test_set)
