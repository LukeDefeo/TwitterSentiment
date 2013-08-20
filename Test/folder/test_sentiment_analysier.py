from NLP_Engine.sentiment_analyser.sentiment_analyser import SentimentAnalyser
from unittest import TestCase
import unittest

__author__ = 'Luke'


class TestSentiment(TestCase):
    def test_sentiment(self):
        classifyer = SentimentAnalyser()
        self.assertEqual(classifyer.classify_tweet('omg justin bieber is so amazing'), 'pos')
        self.assertEqual(classifyer.classify_tweet('fml i hate my xbox'), 'neg')

if __name__ == '__main__':
        unittest.main()
