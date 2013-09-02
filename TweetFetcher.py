from Queue import Queue
import threading
from NLP.Common.helper import pop_slice

__author__ = 'Luke'
from TwitterSearch import TwitterSearchOrder, TwitterSearch, TwitterSearchException
from NLP.sentiment_analyser.sentiment_analyser import classify_tweet, classify_tweet_better
from NLP.sentiment_detector.sentiment_detector_nb import tweet_contains_sentiment

consumer_key = 'ZYaUAuc8zNPM0BL5HgdSSg'
consumer_secret = 'x0Xpf6d6P4nHN2GYl91XOK032ppjhCYOIQCQQT9wA'
access_token = '289934046-1sJjC4Oz1OGT3LYnKgoLGRUehicilfgzMR4TrS6v'
access_token_secret = 'qlulCQHYvEKBQFyPOHcuvrsVUalSmWh2hCHbyhv4'


def replace_hashtag(query):
    if query[0] == '#':
        return '%23' + query[1:]
    else:
        return query


class TweetFetcher(object):
    def __init__(self, query, max_tweets=500):
        self.GUID = 0
        self.query_terms = [replace_hashtag(word) for word in query.split()]
        self.count = 0
        self.MAX_TWEETS = max_tweets
        self.tso = TwitterSearchOrder()
        self.tso.setKeywords(self.query_terms)
        self.tso.setLanguage('en')
        self.tweets_per_page = 100
        self.tso.setCount(self.tweets_per_page)
        self.tso.setIncludeEntities(False)
        self.twitter_search = TwitterSearch(consumer_key, consumer_secret, access_token, access_token_secret)

    def get_tweets(self):
        output = []
        unique_tweets = set()
        try:
            for tweet in self.twitter_search.searchTweetsIterable(self.tso):
                self.GUID += 1
                if self.GUID > self.MAX_TWEETS:
                    break
                if tweet['text'] not in unique_tweets:
                    unique_tweets.add(tweet['text'])
                    output.append({'guid': self.GUID, 'id': tweet['id'], 'text': tweet['text'], 'query': self.query_terms})

        except TwitterSearchException as e:
            print e

        print len(output)
        return output


class TweetStore(object):
    def __init__(self, query):
        self._classified_tweets = []
        self._objective_tweets = []
        self._neutral_tweets = []
        self._tweet_fetcher = TweetFetcher(query)
        self.query = query
        self._unclassified_tweets = self._tweet_fetcher.get_tweets()
        self._all_tweets = []

    def classify_batch(self):
        tweets = pop_slice(self._unclassified_tweets, 10)
        for tweet in tweets:
            if tweet_contains_sentiment(tweet['text']) == 'sub':
                sentiment = classify_tweet_better(tweet['text'], tweet['query'])
                if sentiment == 'unsure':
                    tweet['contains_sentiment'] = False
                    print 'UNSURE - ' + tweet['text']
                    self._neutral_tweets.append(tweet)
                else:
                    tweet['contains_sentiment'] = True
                    self._classified_tweets.append(tweet)

                tweet['sentiment'] = sentiment

            else:
                tweet['contains_sentiment'] = False
                self._objective_tweets.append(tweet)
                print "OBJECTIVE TWEET " + tweet['text']

            self._all_tweets.append(tweet)

    def tweets_remain(self):
        if len(self._unclassified_tweets) > 0:
            return True
        else:
            return False

    def get_latest_tweets(self, start):
        return self._classified_tweets[start:]

    def get_latest_tweets_all(self,start):
        return self._all_tweets[start:]


class TweetProcessor(threading.Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, verbose=None):
        super(TweetProcessor, self).__init__(group, target, name, args, kwargs, verbose)
        self.work_queue = Queue()
        self.daemon = True

    def addJob(self, store):
        self.work_queue.put(store)

    def run(self):
        super(TweetProcessor, self).run()
        while True:
            store = self.work_queue.get()
            store.classify_batch()
            if store.tweets_remain():
                self.work_queue.put(store)
            else:
                print 'done classifying ' + store.query
