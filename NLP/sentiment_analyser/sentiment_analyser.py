import cPickle as pickle
import os
import math
from NLP.Common.helper import neighborhood, contains_negative_emoticon, contains_positive_emoticon
from NLP.Common.tokeniser import tokenise, negations, contains_url


__author__ = 'Luke'
path_to_classifier = '../../Data/Models/sentiment-analyser.obj'
path_to_wordset = "../../Data/Training/word_set-small.obj"
print 'using analysiser ' + path_to_classifier
print 'using wordset ' + path_to_wordset
word_set = pickle.load(open(os.path.join(os.path.dirname(__file__), path_to_wordset)))
classifier = pickle.load(open(os.path.join(os.path.dirname(__file__), path_to_classifier)))
print 'Sentiment Analyser ready...'


def classify_tweet_better(tweet, query_terms):
    empirical_result = empirical_check(tweet)
    if empirical_result is not None:
        return empirical_result
    feature_set = extract_tweet_features(tweet, query_terms)
    probabilities = classifier.prob_classify(feature_set)
    neg_prob = math.pow(10, probabilities._prob_dict['neg'])
    pos_prob = math.pow(10, probabilities._prob_dict['pos'])
    confidence = math.fabs(neg_prob - pos_prob)
    no_words = len(tweet.split())
    threshold = 0.03

    # print str(confidence) + probabilities.max()
    if confidence > 0.1:
        return probabilities.max()
    else:
        return 'unsure'


def classify_tweet(tweet, query_terms=[]):
    empirical_result = empirical_check(tweet)
    if empirical_result is not None:
        return empirical_result

    feature_set = extract_tweet_features(tweet, query_terms)
    return classifier.classify(feature_set)


def empirical_check(tweet):

    tokens = [token for token in tweet.split() if not contains_url(token)]
    tweet = ' '.join(tokens)
    if contains_negative_emoticon(tweet):
        return 'neg'
    if contains_positive_emoticon(tweet):
        return 'pos'
    return None


def extract_tweet_features(tweet, query_terms=[]):
    tokenised_words = [tokenise(word) for word in tweet.split()]
    for word in query_terms:
        try:
            tokenised_words.remove(word)
        except Exception as e:
            pass

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
