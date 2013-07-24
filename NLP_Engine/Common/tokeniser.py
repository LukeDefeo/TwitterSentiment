#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import string

__author__ = 'Luke'


def contains_url(word):
    url_pattern = r'(\S+\.(com|co\.uk|ac|info|ly|net|org|edu|gov)(\/\S+)?)|http://'
    if re.match(url_pattern, word):
        return True
    else:
        return False


def strip_punctuation(word):
    return word.translate(None, string.punctuation)


def contains_foreign_chars(word):
    # pattern = r'![\w\s]'
    # pattern2 = r'[^(\x20-\x7F)]'
    # if re.match(pattern2, word):
    #     return True
    # else:
    #     return False
    exceptions = '£€'
    for char in word:
        if ord(char) > 127:
            if char not in exceptions:
                return True

    return False


def contains_repeated_chars(word, pos=0):
    if len(word) == pos:
        return False

    if len(word) - pos >= 3:
        if word[pos] == word[pos + 1] == word[pos + 2]:
            return True
        else:
            return contains_repeated_chars(word, pos + 1)
    else:
        return False



