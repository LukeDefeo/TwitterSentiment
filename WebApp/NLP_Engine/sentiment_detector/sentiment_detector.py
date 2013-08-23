import cPickle as pickle
import os
import re
from nltk.tag.stanford import POSTagger
from WebApp.NLP_Engine.Common.helper import contains_rolling_letters, contains_trigger_words, contains_caps, contains_emoticons
from WebApp.NLP_Engine.Common.tokeniser import tokenise, strip_punctuation, tokenise2, remove_repeated_chars

__author__ = 'Luke'

path_to_classifier = '../../../Data/Models/sentiment-detector-svm'
svm = pickle.load(open(os.path.join(os.path.dirname(__file__), path_to_classifier)))
pos_tagger = POSTagger(os.path.join(os.path.dirname(__file__), 'stanford-model.tagger'),
                       os.path.join(os.path.dirname(__file__), 'stanford-postagger.jar'), encoding='utf8')

print 'Sentiment Detecter ready...'


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


def empirical_check(tweet):
    tokens = [tokenise2(word) for word in tweet.split()]
    for token in tokens:
        if contains_rolling_letters(token):
            return 'sub'

    tokens = [remove_repeated_chars(token) for token in tokens]
    if contains_trigger_words(tokens):
        return 'sub'

    if contains_caps(tweet):
        return 'sub'

    if contains_emoticons(tweet):
        return 'sub'

    return None


def tweet_contains_sentiment(tweet):
    emperical_result = empirical_check(tweet)
    if emperical_result is not None:
        return emperical_result
    tagged_tweet = pos_tagger.tag(tweet.split())
    tweet_tag_model = extract_tags(tagged_tweet)
    prediction = svm.predict(tweet_tag_model)
    if prediction == 'sub':
        return True
    else:
        return False


