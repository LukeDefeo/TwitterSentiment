import cPickle as pickle
import os
from WebApp.NLP_Engine.Common.helper import neighborhood, contains_negative_emoticon, contains_positive_emoticon
from WebApp.NLP_Engine.Common.tokeniser import tokenise, negations


__author__ = 'Luke'

path_to_classifier = '../../../Data/Models/sentiment-analyser.obj'
path_to_wordset = "../../../Data/Training/word_set-small.obj"
word_set = pickle.load(open(os.path.join(os.path.dirname(__file__), path_to_wordset)))
classifier = pickle.load(open(os.path.join(os.path.dirname(__file__), path_to_classifier)))
print 'Sentiment Analyser ready...'


def classify_tweet(tweet, query_terms=[]):
    empirical_result = empirical_check(tweet)
    if empirical_result is not None:
        return empirical_result

    feature_set = extract_tweet_features(tweet)
    return classifier.classify(feature_set)


def empirical_check(tweet):
    if contains_negative_emoticon(tweet):
        return 'neg'
    if contains_positive_emoticon(tweet):
        return 'pos'
    return None


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