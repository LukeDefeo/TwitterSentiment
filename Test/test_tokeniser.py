#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
__author__ = 'Luke'

from unittest import TestCase
import unittest
from Experimental.Common.tokeniser import *

class test_tokenizer(TestCase):

    def test_contains_url(self):
        urls = ['www.abc.com', 'http://www.cwac.co.uk/dwad', 'https://dwda.org/dwad', 'twitpic.com/wdadawdd']
        for url in urls:
            self.assertTrue(contains_url(url))

    def test_strip_punctuation(self):
        words = [ 'sentence,', 'with.', 'lots?', 'of',  'strange!', 'strange', 'stange...', 'punctuation']
        for word in words:
            word = strip_punctuation(word)
            self.assertTrue(char not in word for char in string.punctuation)

    def test_contains_foreign_chars(self):
        string1 = 'This is a regular english text  '
        string2 = 'with punctuation ! )( ; . > ? '
        string3 = 'and numbers 321 4104'

        self.assertFalse(contains_foreign_chars(string1))
        self.assertFalse(contains_foreign_chars(string2))
        self.assertFalse(contains_foreign_chars(string3))

        string4 = 'ó, ò, ñ ç, ¿, ß'
        self.assertFalse(contains_foreign_chars(string4))


if __name__ == '__main__':
    unittest.main()

