from NLP_Engine.Common.tokeniser import tokenise

__author__ = 'Luke'
import cPickle as pickle
import nltk
from nltk import NaiveBayesClassifier


tweets = pickle.load(open("../../Data/Training/tweets-small.obj"))
word_set = pickle.load((open("../../Data/Training/word_set-small.obj")))

# tweets = pickle.load(open("../../Data/Training/tweets-small.obj"))
# word_set = pickle.load((open("../../Data/Training/word_set-small.obj")))


def tweet_features(tweet):
    tweet_words = tweet.split()
    tokenised_words = set([tokenise(word) for word in tweet_words])

    features = {}
    for dex in range(1, len(tokenised_words)):
        if tweet_words[dex - 1] in word_set and tweet_words[dex] in word_set:
            features[tweet_words[dex - 1] + " " + tweet_words[dex]] = True
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
print classifier.show_most_informative_features(100)
__author__ = 'Luke'

