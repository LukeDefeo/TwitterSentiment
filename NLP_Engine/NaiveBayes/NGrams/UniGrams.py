import time


__author__ = 'Luke'

import nltk
from NLP_Engine.Common.tokeniser import *
import random
import string
from nltk import NaiveBayesClassifier



#read data

start_time = time.time()
tweets = []
i = 0

words = set()


word_dict = dict()

def add_to_dict(word):
    if contains_url(word):
        return
    if contains_repeated_chars(word):
        return
    if word[0] == '@':
        return

    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1


def add_word_to_set(word):
    if contains_url(word):
        return
    if contains_repeated_chars(word):
        return
    if word[0] == '@':
        return

    word = word.translate(None, string.punctuation)
    words.add(word)


with open("/Users/Luke/Documents/PyCharmProjects/TwitterSentiment/Data/Training/training-data.csv") as training_in:
    for line in training_in:
        sentiment, tweet_content = line.split('\t', 1)
        if contains_foreign_chars(tweet_content):
            continue
        tweets.append((sentiment, tweet_content))
        for word in tweet_content.split():
            # add_word_to_set(word.lower())
            add_to_dict(word)
        i += 1
        # if i == 1200:
        #     break

for key in word_dict.keys():
    if word_dict[key] < 3:
        word_dict.pop(key)

# print words
# print words
# print len(words)

print len(word_dict)

print "done " + str(time.time() - start_time) + 's'


reviews = [(movie_reviews.words(fileid), category)
           for category in movie_reviews.categories()
           for fileid in movie_reviews.fileids(category)]

random.shuffle(reviews)

all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
common_words = all_words.keys()[:2000]


def tweet_features(tweet):
    tweet_words = set(tweet)
    features = {}
    for word in common_words:
        features["contains(%s)" % word] = (word in doc_words)

    return features

#generate feature set tuples, dict of features and catagory
feature_set = [(doc_features(doc), cat) for (doc, cat) in reviews]

cut_off = int(0.8 * len(feature_set))
train_set = feature_set[:cut_off]
test_set = feature_set[cut_off:]
classifier = NaiveBayesClassifier.train(train_set)

print nltk.classify.accuracy(classifier, test_set)
