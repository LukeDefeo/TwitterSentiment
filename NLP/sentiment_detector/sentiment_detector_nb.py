import os
import pickle
from NLP.sentiment_detector.build_sentiment_detector_nb import extract_tweet_features_for_detection
from NLP.sentiment_detector.detector_helper import empirical_check

__author__ = 'Luke'


classifier = pickle.load(open(os.path.join(os.path.dirname(__file__), '../../Data/Models/sentiment-detector-nb.obj')))
print classifier.show_most_informative_features(1000)
def tweet_contains_sentiment(tweet):
    emperical_result = empirical_check(tweet)
    if emperical_result is not None:
        return emperical_result

    features = extract_tweet_features_for_detection(tweet)

    return classifier.classify(features)

