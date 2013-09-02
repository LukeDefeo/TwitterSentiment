from NLP.Common.helper import contains_promotional_words, contains_rolling_letters, contains_trigger_words, contains_caps, contains_emoticons
from NLP.Common.tokeniser import contains_url, tokenise2, remove_repeated_chars

__author__ = 'Luke'

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

    if contains_url(tweet):
        print 'contains url'
        return 'obj'
    tokens = [tokenise2(word) for word in tweet.split()]

    if contains_promotional_words(tokens):
        print 'contains promo words'
        return 'obj'

    for token in tokens:
        if contains_rolling_letters(token):
            print 'contains rolling letters'
            return 'sub'

    tokens = [remove_repeated_chars(token) for token in tokens]

    tweet = ' '.join(tokens)
    if contains_caps(tweet):
        print 'Contains lots of caps'
        return 'sub'

    if contains_emoticons(tweet):
        print 'contains emoticons'
        return 'sub'

    return None