from WebApp.NLP_Engine.sentiment_analyser.sentiment_analyser import classify_tweet
from WebApp.NLP_Engine.sentiment_detector.sentiment_detector import tweet_contains_sentiment

__author__ = 'Luke'



print 'type exit to quit'
while True:
    print ""
    sentence = raw_input("Enter a tweet/sentence to analyse...").decode(encoding='utf8')
    if sentence == 'quit':
        break

    if tweet_contains_sentiment(sentence):
        print 'Contains a ' + classify_tweet(sentence) + 'itive sentiment'
    else:
        print 'doesnt contain sentiment'

    print ''