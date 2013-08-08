
__author__ = 'Luke'
import cPickle as pickle
import nltk
from nltk import NaiveBayesClassifier


tweets = pickle.load(open("../../Data/Training/tweets-small.obj.obj"))
word_set = pickle.load((open("../../Data/Training/word_set-small.obj.obj")))

# tweets = pickle.load(open("../../Data/Training/tweets-small.obj.obj"))
# word_set = pickle.load((open("../../Data/Training/word_set-small.obj.obj")))


def tweet_features(tweet):
    tweet_words = set(tweet.split())
    features = {}
    for word in tweet_words:
        if word in word_set:
            features["contains(%s)" % word] = True
    return features


test_set = []
with open("../../Data/Test/test-data.csv") as test_in:
    for line in test_in:
        sentiment, tweet_content = line.split('\t', 1)
        test_set.append((tweet_features(tweet_content), sentiment))

print 'done making test'

print test_set

train_set = [(tweet_features(tweet), sentiment) for (tweet, sentiment) in tweets]

print "starting classififyer building"
classifier = NaiveBayesClassifier.train(train_set)

print "done building classifer"
print nltk.classify.accuracy(classifier, test_set)