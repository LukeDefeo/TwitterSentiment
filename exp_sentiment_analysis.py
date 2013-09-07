from NLP.sentiment_analyser.sentiment_analyser import classify_tweet, classify_tweet_better

__author__ = 'Luke'

while True:
    print ' '
    sentence = raw_input('Enter word / sentence to classify... \n')

    result = classify_tweet_better(sentence, [])
    if result == 'pos' or result == 'neg':
        print 'Contains a ' + result + 'itive sentiment'
    else:
        print 'Cannot determine whether positive or negative'
