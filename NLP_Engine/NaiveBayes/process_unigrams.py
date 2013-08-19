from NLP_Engine.Common.tokeniser import tokenise

__author__ = 'Luke'
import cPickle as pickle
import nltk
from nltk import NaiveBayesClassifier

mode = "big"


tweets = pickle.load(open("../../Data/Training/tweets-small.obj"))
word_set = pickle.load((open("../../Data/Training/word_set-small.obj")))

# tweets = pickle.load(open("../../Data/Training/tweets-small.obj"))
# word_set = pickle.load((open("../../Data/Training/word_set-small.obj")))
#

def tweet_features(tweet):
    tweet_words = tweet.split()
    tokenised_words = set([tokenise(word) for word in tweet_words])

    features = {}
    for word in tokenised_words:
        if word in word_set:
            features[word] = True
    return features


test_set = []
with open("../../Data/Test/test-data.csv") as test_in:
    for line in test_in:
        sentiment, tweet_content = line.split('\t', 1)
        test_set.append((tweet_features(tweet_content), sentiment))

print 'done making test set'

train_set = [(tweet_features(tweet), sentiment) for (tweet, sentiment) in tweets]
print 'done making training set'

print "starting classififyer building"
classifier = NaiveBayesClassifier.train(train_set)

print "done building classifer"
print nltk.classify.accuracy(classifier, test_set)

# for (feature_set, sent) in train_set:
#     for key in feature_set.keys():
#         print key,
#     print ""
#     print "prediction - " + classifier.classify(feature_set)
#     print "actual - " + sent
#     print classifier.prob_classify(feature_set)._prob_dict
#


print classifier.show_most_informative_features(1000)
