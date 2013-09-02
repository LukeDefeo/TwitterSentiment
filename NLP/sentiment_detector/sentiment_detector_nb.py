import os
import pickle
from NLP.sentiment_analyser.sentiment_analyser import empirical_check
from NLP.sentiment_detector.build_sentiment_detector_nb import extract_tweet_features_for_detection

__author__ = 'Luke'


classifier = pickle.load(open(os.path.join(os.path.dirname(__file__), '../../Data/Models/sentiment-detector-nb.obj')))

def tweet_contains_sentiment(tweet):
    emperical_result = empirical_check(tweet)
    if emperical_result is not None:
        return emperical_result

    features = extract_tweet_features_for_detection(tweet)

    return classifier.classify(features)

