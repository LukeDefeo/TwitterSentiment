import cPickle as pickle
from nltk.tag.stanford import POSTagger
from WebApp.NLP_Engine.sentiment_detector.sentiment_detector import extract_tags

__author__ = 'Luke'

print 'begin'
#testing the classifyer on completely unseen training data
svm = pickle.load(open('../../Data/Models/sentiment-detector-svm'))
test_set = []
with open("../../Data/Test/test-data.csv") as test_in:
    for line in test_in:
        sentiment, tweet_content = line.split('\t', 1)
        if sentiment == 'neg' or sentiment == 'pos':
            sentiment = 'sub'
        elif sentiment == 'neutral':
            sentiment = 'obj'
        else:
            print 'error'
        test_set.append((tweet_content, sentiment))

print len(test_set)
tagger = POSTagger('stanford-model.tagger', 'stanford-postagger.jar', encoding='utf8')

test_data = pickle.load(open('../../Data/Test/sentiment-detector.obj'))
targets = [label for sent, label in test_set]

print svm.score(test_data, targets)
