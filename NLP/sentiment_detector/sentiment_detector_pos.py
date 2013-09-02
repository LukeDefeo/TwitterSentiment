import cPickle as pickle
import os
from nltk.tag.stanford import POSTagger
from NLP.Common.tokeniser import contains_url
from NLP.sentiment_detector.detector_helper import empirical_check, extract_tags

__author__ = 'Luke'

path_to_classifier = '../../Data/Models/sentiment-detector-svm'
print 'Using detector: ' + path_to_classifier
svm = pickle.load(open(os.path.join(os.path.dirname(__file__), path_to_classifier)))
pos_tagger = POSTagger(os.path.join(os.path.dirname(__file__), 'stanford-model.tagger'),
                       os.path.join(os.path.dirname(__file__), 'stanford-postagger.jar'), encoding='utf8')

print 'Sentiment Detecter ready...'


def tokenise_for_POS(tweet):
    tokens = [token for token in tweet.split() if not contains_url(token)]
    return tokens

def tweet_contains_sentiment(tweet):
    emperical_result = empirical_check(tweet)
    if emperical_result is not None:
        return emperical_result
    tokens = tokenise_for_POS(tweet)
    tagged_tweet = pos_tagger.tag(tokens)
    tweet_tag_model = extract_tags(tagged_tweet)
    prediction = svm.predict(tweet_tag_model)
    return prediction


