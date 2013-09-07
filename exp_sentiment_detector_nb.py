import os
import pickle
from NLP.sentiment_detector.build_sentiment_detector_nb import extract_tweet_features_for_detection

__author__ = 'Luke'

classifier = pickle.load(open(os.path.join(os.path.dirname(__file__), 'Data/Models/sentiment-detector-nb.obj')))

while True:
    sent = raw_input("Enter sentence...\n")
    features = extract_tweet_features_for_detection(sent)
    res = classifier.classify(features)
    if res == 'sub':
        print 'Sentence is Subjective'
    else:
        print 'Sentence is Objective'