import os
import pickle
import random
from nltk import NaiveBayesClassifier
import nltk
from NLP.Common.tokeniser import tokenise

__author__ = 'Luke'
path_to_wordset = "../../Data/Training/word_set-detector.obj"
word_set = pickle.load(open(os.path.join(os.path.dirname(__file__), path_to_wordset)))

def extract_tweet_features_for_detection(tweet):
    tokenised_words = set([tokenise(word) for word in tweet.split()])
    features = {}
    for word in tokenised_words:
        if word in word_set:
            features[word] = True
    return features


if __name__ == '__main__':

    objective_tweets = pickle.load(open('../../Data/Training/objective-tweets.obj'))
    print len(objective_tweets)
    subjective_tweets = pickle.load(open('../../Data/Training/subjective-tweets.obj'))
    print len(subjective_tweets)
    objective_tweets = [(tweet, u'obj') for tweet in objective_tweets]
    subjective_tweets = [(tweet, u'sub') for tweet in subjective_tweets]
    total_set = objective_tweets + subjective_tweets
    random.shuffle(total_set)
    cut_off = int(0.85 * len(total_set))



    total_set = [(extract_tweet_features_for_detection(tweet), sentiment) for (tweet, sentiment) in total_set]
    training_data = total_set[:cut_off]
    test_data = total_set[cut_off:]
    classifier = NaiveBayesClassifier.train(training_data)

    print nltk.classify.accuracy(classifier, test_data)

    test_set = []
    with open("../../Data/Test/test-data.csv") as test_in:
        for line in test_in:
            sentiment, tweet_content = line.split('\t', 1)
            if sentiment == 'neg' or sentiment == 'pos':
                sentiment = 'sub'
            elif sentiment == 'neutral':
                sentiment = 'obj'
            else:
                print 'error'
            test_set.append((tweet_content, sentiment))

    test_set = [(extract_tweet_features_for_detection(tweet), sentiment) for (tweet, sentiment) in test_set]
    print nltk.classify.accuracy(classifier, test_set)
    print classifier.show_most_informative_features(1000)

    pickle.dump(classifier, open('../../Data/Models/sentiment-detector-nb.obj', 'wb'))