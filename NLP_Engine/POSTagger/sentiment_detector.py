import random

from nltk.tag.stanford import POSTagger
from sklearn.svm import SVC
from NLP_Engine.Common.helper import extract_tags


__author__ = 'Luke'
import cPickle as pickle


def tokenise_tweet():
    pass



objective_tweets = pickle.load(open('../../Data/Training/objective-tweets.obj'))
subjective_tweets = pickle.load(open('../../Data/Training/subjective-tweets.obj'))

objective_tweets = [(tweet, u'obj') for tweet in objective_tweets]
subjective_tweets = [(tweet, u'sub') for tweet, sent in subjective_tweets]
#
# objective_tweets = objective_tweets[:100]
# subjective_tweets = subjective_tweets[:100]

total_set = objective_tweets + subjective_tweets
random.shuffle(total_set)
cut_off = int(0.85*len(total_set))

tagger = POSTagger('stanford-model.tagger', 'stanford-postagger.jar', encoding='utf8')

tagged_set = tagger.batch_tag([sent.split() for sent, label in total_set])

total_target = [label for sent, label in total_set]

to_disk = zip(tagged_set, total_target)
print len(tagged_set)
print len(total_set)
pickle.dump(to_disk, open('../../Data/Training/sentiment_detector_training.obj', 'wb'))

total_data = [extract_tags(sent) for sent in tagged_set]
training_data = total_data[:cut_off]
test_data = total_data[cut_off:]

training_target = total_target[:cut_off]
test_target = total_target[cut_off:]

svm = SVC()
svm.fit(training_data, training_target)
print svm.score(test_data,test_target)

print subjective_tweets[0]
print objective_tweets[0]
print len(objective_tweets)
print len(subjective_tweets)

