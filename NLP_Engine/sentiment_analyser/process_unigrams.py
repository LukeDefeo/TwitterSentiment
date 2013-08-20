from NLP_Engine.Common.helper import neighborhood
from NLP_Engine.Common.tokeniser import tokenise, negations

__author__ = 'Luke'
import cPickle as pickle
import nltk
from nltk import NaiveBayesClassifier


tweets = pickle.load(open("../../Data/Training/tweets-small.obj"))
word_set = pickle.load((open("../../Data/Training/word_set-small.obj")))

# tweets = pickle.load(open("../../Data/Training/tweets-small.obj"))
# word_set = pickle.load((open("../../Data/Training/word_set-small.obj")))
#

def tweet_features(tweet):
    tokenised_words = [tokenise(word) for word in tweet.split()]
    to_remove = set()
    # print tokenised_words
    for prev, word, next in neighborhood(tokenised_words):
        if prev in negations:
            to_remove.add(prev)
            to_remove.add(word)
            tokenised_words.append('neg-' + word)

    tokenised_words = set(tokenised_words)
    for word in to_remove:
        tokenised_words.remove(word)

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

pickle.dump(classifier, open('../../Data/Models/sentiment-analyser.obj','wb'))