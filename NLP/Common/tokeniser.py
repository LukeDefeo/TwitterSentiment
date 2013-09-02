#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import string
from nltk import PorterStemmer
import sklearn


__author__ = 'Luke'
negations = {'no', 'not', 'never', "don't", 'dont', 'cant', "can't", 'cannot', 'wont','isnt',"isn't",'aint'}
promotional_base = {'bargain', 'deal', 'competition', 'win', 'won', 'promotion','sale'}
promotional = set()
stemmer =  PorterStemmer()

for word in promotional_base:
    promotional.add(word)
    promotional.add(word + 's')
    promotional.add('#' + word)
    promotional.add('#' + word + 's')

def contains_url(word):
    url_pattern = r'(\S+\.(com|co\.uk|ac|info|ly|net|org|edu|gov|to|us|au)(\/\S+)?)|http://'
    url_pattern2 = r'(\S+\.(\S+)(\/\S+))'
    if re.match(url_pattern2, word) or re.match(url_pattern, word):
        return True
    else:
        return False


def strip_punctuation(word):
    while _ends_with_punct(word):
        if len(word) == 1:
            return ''
        word = word[:-1]

    return word


def _ends_with_punct(word):
    for punct in string.punctuation:
        if word.endswith(punct):
            return True
    return False


def contains_foreign_chars(word):
    exceptions = u'£€'
    for char in word:
        if ord(char) > 127:
            if char not in exceptions:
                return True

    return False


def remove_repeated_chars(word):
    pos = 0
    while len(word) - pos >= 3:
        if word[pos] == word[pos + 1] == word[pos + 2]:
            while word[pos] == word[pos + 1]:
                word = delete_char(word, pos)
                if pos == len(word) - 1:
                    break
        else:
            pos += 1
    return word


def delete_char(word, index):
    return word[:index] + word[index + 1:]


def tokenise_tweet(tweet):
    for word in tweet.split():
        if contains_url(word):
            continue

def remove_hashtag(word):
    if len(word) > 0:
        if word[0] == '#':
            return word[1:]

    return word


def tokenise(word):
    if contains_url(word):
        return ''
    if word[0] == '@':
        return ''
    if '&' in word:
        return ''

    word = word.lower()
    word = strip_punctuation(word)
    word = remove_repeated_chars(word)
    word = remove_hashtag(word)
    # word = stemmer.stem_word(word)


    return word


"""special case where we dont remove the repeated chars"""
def tokenise2(word):
    if contains_url(word):
        return ''
        # if contains_repeated_chars(word):
    #     return
    if word[0] == '@':
        return ''
    if '&' in word:
        return ''

    word = word.lower()
    word = strip_punctuation(word)
    return word


