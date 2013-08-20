from NLP_Engine.sentiment_analyser.sentiment_analyser import SentimentAnalyser
from unittest import TestCase
import unittest
from NLP_Engine.sentiment_detector.sentiment_detector import SentimentDetector

__author__ = 'Luke'


class TestSentiment(TestCase):
    def test_sentiment_analysis(self):
        classifyer = SentimentAnalyser()
        self.assertEqual(classifyer.classify_tweet('omg justin bieber is so amazing'), 'pos')
        self.assertEqual(classifyer.classify_tweet('fml i hate my xbox'), 'neg')

    def test_sentiment_detection(self):
        detecter = SentimentDetector()
        self.assertTrue(detecter.tweet_contains_sentiment('omg justin bieber is so amazing '))
        self.assertFalse(detecter.tweet_contains_sentiment(
            'President Obama has just landed in London for the annual conference for world leaders'))


if __name__ == '__main__':
    unittest.main()
