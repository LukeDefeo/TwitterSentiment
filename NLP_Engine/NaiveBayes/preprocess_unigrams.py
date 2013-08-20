from nltk.corpus import stopwords
from NLP_Engine.Common.helper import neighborhood

__author__ = 'Luke'
import time
import cPickle as pickle
from NLP_Engine.Common.tokeniser import *

start_time = time.time()
tweets = []
word_dict = dict()


def add_to_dict(word):
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1



print "begin"
with open("../../Data/Training/training-data.csv") as training_in:
    for line in training_in:
        line = line.decode(encoding='latin1')
        sentiment, tweet_content = line.split('\t', 1)
        if contains_foreign_chars(tweet_content):
            continue

        tweets.append((tweet_content, sentiment))
        for prev, word, after in neighborhood(tweet_content.split()):
            if prev in negations:
                add_to_dict(tokenise(u'neg-' + word))
            else:
                add_to_dict(tokenise(word))

for key in word_dict.keys():
    if word_dict[key] < 5:
        word_dict.pop(key)

words = set(word_dict.keys())
for word in stopwords.words('english'):
    try:
        words.remove(word)
    except:
        pass

print "done " + str(time.time() - start_time) + 'seconds'
print "pickling"
pickle.dump(tweets, open("../../Data/Training/tweets.obj", "wb"))
pickle.dump(words, open("../../Data/Training/word_set.obj", "wb"))

print "done picking " + str(time.time() - start_time) + 'seconds'

