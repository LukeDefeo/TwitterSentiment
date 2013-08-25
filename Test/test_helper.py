from NLP.Common.helper import *
from NLP.Common.tokeniser import tokenise
import unittest
__author__ = 'Luke'

class MyTestCase(unittest.TestCase):

    def test_contains_emoticon(self):
        emoticons = ':) ;-) =) :) :P :-P =) =] ={ :D ;) :/ ;/ :( ;p =/ =['
        for emoticon in emoticons.split():
            self.assertTrue(contains_emoticons(emoticon))

        not_emoticons = 'hello. what: only(there is)more'
        for not_emoticon in not_emoticons:
            self.assertIsNone(contains_emoticons(not_emoticon))

    def test_contrains_positive_emoticon(self):
        positive_emoticons = ':) ;-) =) :) :P :-P =) =] :D ;) ;p =]'
        negative_emoticons = ' ={ :/ ;/ :(  =/ =['
        for pos in positive_emoticons.split():
            self.assertTrue(contains_positive_emoticon(pos))
        for neg in negative_emoticons.split():
            self.assertIsNone(contains_positive_emoticon(neg))

    def test_contrains_negative_emoticon(self):
        positive_emoticons = ':) ;-) =) :) :P :-P =) =] :D ;) ;p =]'
        negative_emoticons = ' ={ :/ ;/ :(  =/ =['
        for neg in negative_emoticons.split():
            self.assertTrue(contains_negative_emoticon(neg))
        for pos in positive_emoticons.split():
            self.assertIsNone(contains_negative_emoticon(pos))


    def test_contains_repeated_chars(self):
        good = 'good ok fine very terrible' #what about numbers 1000?
        bad = 'goooood fineeee :)))))) gggreat what???'

        for word in good.split():
            self.assertFalse(contains_rolling_letters(word))

        for word in bad.split():
            self.assertTrue(contains_rolling_letters(word))

    def test_contains_caps(self):
        emotive_tweets = ['OMG i can THINK I AM GOING TO GET A PS4',]
        objective_tweets = ['A NSA CIA line up for blah blah blah bit.ly/SQUSGX']

        for tweet in emotive_tweets:
            self.assertTrue(contains_caps(tweet))

        for tweet in objective_tweets:
            self.assertFalse(contains_caps(tweet))

    def test_contains_emotive_trigger_words(self):
        emotive_tweets = ['OMG! i can THINK I AM GOING TO GET A PS4',]
        fail = ['i am getting a ps4']
        for tweet in emotive_tweets:
            tokens = [tokenise(word) for word in tweet.split()]
            self.assertTrue(contains_trigger_words(tokens))

        for tweet in fail:
            tokens = [tokenise(word) for word in tweet.split()]
            self.assertFalse(contains_trigger_words(tokens))

if __name__ == '__main__':
    unittest.main()
