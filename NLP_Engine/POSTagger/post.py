import cPickle as pickle
import random
from nltk import NaiveBayesClassifier
import nltk

__author__ = 'Luke'

feature_set = pickle.load(open("../../Data/Training/tagged-sents.obj"))
feature_set = [(tags, cat) for tags, sent, cat in feature_set]
random.shuffle(feature_set)

cut_off = int(0.9 * len(feature_set))
train_set = feature_set[:cut_off]
test_set = feature_set[cut_off:]

print train_set
print test_set

classifier = NaiveBayesClassifier.train(train_set)

print "starting classifyer building"
print nltk.classify.accuracy(classifier, test_set)

print classifier.show_most_informative_features(100)