import random

from nltk.tag.stanford import POSTagger
from sklearn.svm import SVC


__author__ = 'Luke'
import cPickle as pickle


def tokenise_tweet():
    pass



objective_tweets = pickle.load(open('../../../Data/Training/objective-tweets.obj'))
subjective_tweets = pickle.load(open('../../../Data/Training/subjective-tweets.obj'))

objective_tweets = [(tweet, u'obj') for tweet in objective_tweets]
subjective_tweets = [(tweet, u'sub') for tweet, sent in subjective_tweets]
total_set = objective_tweets + subjective_tweets
random.shuffle(total_set)
cut_off = int(0.85*len(total_set))

tagger = POSTagger('stanford-model.tagger', 'stanford-postagger.jar', encoding='utf8')
tagged_sentences = tagger.batch_tag([sent.split() for sent, label in total_set])

target_values = [label for sent, label in total_set]

to_disk = zip(tagged_sentences, target_values)
pickle.dump(to_disk, open('../../../Data/Training/sentiment_detector_training.obj', 'wb'))



