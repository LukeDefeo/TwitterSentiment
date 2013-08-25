import cPickle as pickle
from nltk.tag.stanford import POSTagger
from NLP.sentiment_detector.sentiment_detector import extract_tags

__author__ = 'Luke'

print 'begin'
#testing the classifyer on completely unseen training data
svm = pickle.load(open('../../../Data/Models/sentiment-detector-svm-new'))
test_set = []
with open("../../../Data/Test/test-data.csv") as test_in:
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

tagged_set = tagger.batch_tag([sent.split() for sent, label in test_set])
test_data = [extract_tags(sent) for sent in tagged_set]
pickle.dump(test_data, open('../../../Data/Test/sentiment-detector.obj', 'w+'))

targets = [label for sent, label in test_set]

print svm.score(test_data, targets)
