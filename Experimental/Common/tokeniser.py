import re
import string

__author__ = 'Luke'



def contains_url(word):
    url_pattern = r'(\S+\.(com|co\.uk|ac|info|ly|net|org|edu|gov)(\/\S+)?)'
    if re.match(url_pattern, word):
        return True
    else:
        return False

def strip_punctuation(word):
    return word.translate(None, string.punctuation)

def contains_foreign_chars(word):
    pattern = r''
    if(re.match(pattern,word)):
        return True
    else:
        return False

def tweet_foriegn(tweet):
    pass