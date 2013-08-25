#!/usr/bin/python
# -*- coding: UTF-8 -*-
from NLP.Common.helper import contains_rolling_letters
from NLP.Common.tokeniser import *

__author__ = 'Luke'

from unittest import TestCase
import unittest


class test_tokenizer(TestCase):

    def test_contains_url(self):
        urls = ['www.abc.com', 'http://www.cwac.co.uk/dwad', 'https://dwda.org/dwad', 'twitpic.com/wdadawdd',
                'http://u.nu/9p78', 'pics.byz/sfdsSF']
        not_urls = ['test.', 'only/', 'went...', ':p']

        for url in urls:
            self.assertTrue(contains_url(url))

        for thing in not_urls:
            self.assertFalse(contains_url(thing))


    def test_strip_punctuation(self):
        words = ['sentence,', 'with.', 'lots?', 'of', 'strange!!!', 'strange', 'stange...', 'punctuation']
        for word in words:
            word = strip_punctuation(word)
            self.assertTrue(char not in word for char in string.punctuation)

        trick_word = strip_punctuation("father's")
        self.assertEqual("father's", trick_word)


    def test_contains_foreign_chars(self):
        string1 = u'This is a regular english text '
        string2 = u'with punctuation ! )( ; . > ? and symbols "[ {` ~ +- $'''
        string3 = u'and numbers 321 4104'

        self.assertFalse(contains_foreign_chars(string1))
        self.assertFalse(contains_foreign_chars(string2))
        self.assertFalse(contains_foreign_chars(string3))

        string4 = u'ó ò ñ ç ¿ ß'
        self.assertTrue(contains_foreign_chars(string4))

        string5 = u'dawd ó?'
        self.assertTrue(contains_foreign_chars(string5))


    def test_delete_repeated_chars(self):
        bad = ['ooooh', 'verrrrry', 'loooongggg', 'stunning', 'happyyyyy']
        good = ['oh', 'very', 'long', 'stunning', 'happy']
        result = [remove_repeated_chars(word) for word in bad]
        self.assertEqual(good, result)


    if __name__ == '__main__':
        unittest.main()

