from NLP.sentiment_analyser.sentiment_analyser import extract_tweet_features

__author__ = 'Luke'
import cPickle as pickle
import nltk
from nltk import NaiveBayesClassifier


training_tweets = pickle.load(open("../../Data/Training/tweets-small.obj"))

train_set = [(extract_tweet_features(tweet), sentiment) for (tweet, sentiment) in training_tweets]
print 'done making training set'

test_set = []
with open("../../Data/Test/test-data.csv") as test_in:
    for line in test_in:
        sentiment, tweet_content = line.split('\t', 1)
        test_set.append((extract_tweet_features(tweet_content), sentiment))

print 'done making test set'

print "starting classififyer building"
classifier = NaiveBayesClassifier.train(train_set)
print classifier.show_most_informative_features(1000)
print nltk.classify.accuracy(classifier, test_set)

print 'Saving model to disk'
pickle.dump(classifier, open('../../Data/Models/sentiment-analyser.obj','wb'))