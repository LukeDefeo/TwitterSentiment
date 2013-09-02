from NLP.sentiment_analyser.sentiment_analyser import classify_tweet, classify_tweet_better
from NLP.sentiment_detector.sentiment_detector import tweet_contains_sentiment

__author__ = 'Luke'


print 'Type quit to exit.'
while True:
    print ' '
    sentence = raw_input('Enter sentence to classify')
    if tweet_contains_sentiment(sentence) == 'sub':
        print 'Contains a ' + str(classify_tweet_better(sentence,[])) + 'itive sentiment'
    else:
        print "Doesn't contain a sentiment"