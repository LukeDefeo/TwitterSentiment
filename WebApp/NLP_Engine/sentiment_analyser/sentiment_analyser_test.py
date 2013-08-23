from WebApp.NLP_Engine.sentiment_analyser.sentiment_analyser import classify_tweet

__author__ = 'Luke'




while True:
    print 'type exit to quit'
    sentence = raw_input("Enter a tweet/sentence to analyse...").decode(encoding='utf8')
    if sentence == 'quit':
        break

    print classify_tweet(sentence) + sentence