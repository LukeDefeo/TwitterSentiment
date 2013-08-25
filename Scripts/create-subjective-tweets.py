import pickle
import random
from NLP.Common.tokeniser import contains_foreign_chars

__author__ = 'Luke'

print 'start '

tweets = []
pos = 0
neg = 0
print "begin"
i = 0
with open("../Data/Training/training-data-small.csv") as training_in:
    for line in training_in:
        line = line.decode(encoding='latin1')
        sentiment, tweet_content = line.split('\t', 1)

        if contains_foreign_chars(tweet_content):
            continue

        if sentiment == 'pos':
            pos += 1
        else:
            neg += 1

        tweets.append(tweet_content)


print  pos
print neg
print len(tweets)
random.shuffle(tweets)
tweets = tweets[:20000]
pickle.dump(tweets, open('../Data/Training/subjective-tweets.obj', 'wb'))