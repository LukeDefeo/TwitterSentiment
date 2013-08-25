from unittest import TestCase
import unittest
from NLP.sentiment_analyser.sentiment_analyser import classify_tweet
from NLP.sentiment_detector.sentiment_detector import tweet_contains_sentiment

__author__ = 'Luke'


class TestSentiment(TestCase):
    def test_sentiment_analysis(self):
        self.assertEqual(classify_tweet('omg justin bieber is so amazing'), 'pos')
        self.assertEqual(classify_tweet('fml i hate my xbox'), 'neg')

    def test_sentiment_detection(self):
        self.assertTrue(tweet_contains_sentiment('omg justin bieber is so amazing '))
        self.assertFalse(tweet_contains_sentiment(
            'President Obama has just landed in London for the annual conference for world leaders'))


if __name__ == '__main__':
    unittest.main()
