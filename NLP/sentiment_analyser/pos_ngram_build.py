from NLP.Common.helper import neighborhood
from NLP.Common.tokeniser import negations, tokenise
from NLP.sentiment_analyser.sentiment_analyser import extract_tweet_features

__author__ = 'Luke'
import cPickle as pickle
import nltk
from nltk import NaiveBayesClassifier

word_dict = dict()


def add_to_dict(word, tag):
    combo = word + '-' + tag
    if combo in word_dict:
        word_dict[combo] += 1
    else:
        word_dict[combo] = 1


training_tweets = pickle.load(
    open("/Users/Luke/Documents/PyCharmProjects/TwitterSentiment/Data/Training/tweets-pos.obj"))
for item in training_tweets:
    tagged_sent = item[0][0]
    for prev, word, after in neighborhood(tagged_sent):
        if prev is not None and prev[0] in negations:
            add_to_dict(tokenise(u'neg-' + word[0]), word[1])
        else:
            add_to_dict(tokenise(word), word[1])

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
pickle.dump(classifier, open('../../Data/Models/sentiment-analyser-pos.obj', 'wb'))