import cPickle as pickle
import os
from nltk.tag.stanford import POSTagger

__author__ = 'Luke'


path_to_classifier = '../../Data/Models/sentiment-detector-svm'
svm = pickle.load(open(os.path.join(os.path.dirname(__file__), path_to_classifier)))
pos_tagger = POSTagger(os.path.join(os.path.dirname(__file__), 'stanford-model.tagger'),
                       os.path.join(os.path.dirname(__file__), 'stanford-postagger.jar'), encoding='utf8')


def extract_tags(tagged_sent):
    tags = [0] * len(tag_index)
    for word, tag in tagged_sent:
        tags[tag_index[tag]] += 1

    return tags


"from tagset used in stanford tagger: http://acl.ldc.upenn.edu/J/J93/J93-2004.pdf"
tag_index = {'CC': 0, 'CD': 1, 'DT': 2, 'EX': 3, 'FW': 4, 'IN': 5, 'JJ': 6, 'JJR': 7, 'JJS': 8, 'LS': 9, 'MD': 10,
             'NN': 11, 'NNS': 12, 'NNP': 13, 'NNPS': 14, 'PDT': 15, 'POS': 16, 'PRP': 17, 'PP$': 18, 'RB': 19,
             'RBR': 20, 'RBS': 21, 'RP': 22, 'SYM': 23, 'TO': 24, 'UH': 25, 'VB': 26, 'VBD': 27, 'VBG': 28, 'VBN': 29,
             'VBP': 30, 'VBZ': 31, 'WDT': 32, 'WP': 33, 'WP$': 34, 'WRB': 35, '#': 36, '$': 37, '.': 38, ',': 39,
             ':': 40, '(': 41, ')': 42, '"': 43, "'": 44, "``": 45, "''": 46, 'PRP$': 47}



def tweet_contains_sentiment(tweet):
    tagged_tweet = pos_tagger.tag(tweet.split())
    tweet_tag_model = extract_tags(tagged_tweet)
    prediction = svm.predict(tweet_tag_model)
    if prediction == 'sub':
        return True
    else:
        return False


