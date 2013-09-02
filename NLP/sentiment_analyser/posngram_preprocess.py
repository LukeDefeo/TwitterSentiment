import os
from nltk.corpus import stopwords
from nltk.tag.stanford import POSTagger
from NLP.Common.helper import neighborhood
from NLP.Common.tokeniser import contains_foreign_chars, negations, tokenise, contains_url, remove_hashtag

__author__ = 'Luke'
import time
import cPickle as pickle

start_time = time.time()
tweets = []
word_dict = dict()


def remove_user(word):
    if len(word) > 0:
        if word[0] == '@':
            return 'Username'

    return word


def tokenise_for_POS(tweet):
    tokens = [remove_hashtag(remove_user(token)) for token in tweet.split() if not contains_url(token)]
    return tokens


pos_tagger = POSTagger(os.path.join(os.path.dirname(__file__), '../sentiment_detector/stanford-model.tagger'),
                       os.path.join(os.path.dirname(__file__), '../sentiment_detector/stanford-postagger.jar'),
                       encoding='utf8',java_options='-Xmx4000m')


def add_to_dict(word):
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1


print "begin"
with open("../../Data/Training/training-data-small.csv") as training_in:
    for line in training_in:
        line = line.decode(encoding='latin1')
        sentiment, tweet_content = line.split('\t', 1)
        if contains_foreign_chars(tweet_content):
            continue

        tweets.append((tokenise_for_POS(tweet_content), sentiment))
        for prev, word, after in neighborhood(tweet_content.split()):
            if prev in negations:
                add_to_dict(tokenise(u'neg-' + word))
            else:
                add_to_dict(tokenise(word))

sentences, sentiments = zip(*tweets)
sentences = pos_tagger.batch_tag(sentences)
tweets = zip(sentences, sentiments)
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
pickle.dump(tweets, open("../../Data/Training/tweets-pos.obj", "wb"))
pickle.dump(words, open("../../Data/Training/word_set-pos.obj", "wb"))

print "done: " + str(time.time() - start_time) + 'seconds'

