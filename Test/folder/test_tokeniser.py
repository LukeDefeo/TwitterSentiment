#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'Luke'

from unittest import TestCase
import unittest
from NLP_Engine.Common.tokeniser import *


class test_tokenizer(TestCase):

    def test_contains_url(self):
        urls = ['www.abc.com', 'http://www.cwac.co.uk/dwad', 'https://dwda.org/dwad', 'twitpic.com/wdadawdd','http://u.nu/9p78']
        for url in urls:
            self.assertTrue(contains_url(url))

    def test_strip_punctuation(self):
        words = [ 'sentence,', 'with.', 'lots?', 'of',  'strange!!!', 'strange', 'stange...', 'punctuation']
        for word in words:
            word = strip_punctuation(word)
            self.assertTrue(char not in word for char in string.punctuation)

        trick_word = strip_punctuation("father's")
        self.assertEqual("father's",trick_word)


    def test_contains_foreign_chars(self):
        string1 = 'This is a regular english text '
        string2 = 'with punctuation ! )( ; . > ? and symbols "[ {` ~ +- $'''
        string3 = 'and numbers 321 4104'

        self.assertFalse(contains_foreign_chars(string1))
        self.assertFalse(contains_foreign_chars(string2))
        self.assertFalse(contains_foreign_chars(string3))

        string4 = 'ó ò ñ ç ¿ ß'
        self.assertTrue(contains_foreign_chars(string4))

        string5 = 'dawd ó?'
        self.assertTrue(contains_foreign_chars(string5))

    def test_contains_repeated_chars(self):
        good = 'good ok fine very' #what about numbers 1000?
        bad = 'goooood fineeee :)))))) gggreat'

        for word in good.split():
            self.assertFalse(contains_repeated_chars(word))

        for word in bad.split():
            self.assertTrue(contains_repeated_chars(word))

    def test_delete_repeated_chars(self):
        bad = ['ooooh', 'verrrrry', 'loooongggg','stunning','happyyyyy']
        good = ['oh','very','long','stunning']
        result = [remove_repeated_chars(word) for word in bad]
        print result

        self.assertEqual(good,result)


    if __name__ == '__main__':
        unittest.main()

