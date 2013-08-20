import cPickle as pickle
from NLP_Engine.Common.helper import neighborhood
from NLP_Engine.Common.tokeniser import tokenise, negations


__author__ = 'Luke'
word_set = pickle.load(open("../../Data/Training/word_set-small.obj"))


class SentimentAnalyser(object):
    def __init__(self, path_to_classifer='../../Data/Models/sentiment-analyser.obj'):
        self._classifier = pickle.load(open(path_to_classifer))

    def classify_tweet(self, tweet):
        feature_set = extract_tweet_features(tweet)
        return self._classifier.classify(feature_set)


def extract_tweet_features(tweet):
    tokenised_words = [tokenise(word) for word in tweet.split()]
    to_remove = set()
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