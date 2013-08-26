from Queue import Queue
import threading

__author__ = 'Luke'
from TwitterSearch import TwitterSearchOrder, TwitterSearch, TwitterSearchException
from NLP.sentiment_analyser.sentiment_analyser import classify_tweet
from NLP.sentiment_detector.sentiment_detector import tweet_contains_sentiment

consumer_key = 'ZYaUAuc8zNPM0BL5HgdSSg'
consumer_secret = 'x0Xpf6d6P4nHN2GYl91XOK032ppjhCYOIQCQQT9wA'
access_token = '289934046-1sJjC4Oz1OGT3LYnKgoLGRUehicilfgzMR4TrS6v'
access_token_secret = 'qlulCQHYvEKBQFyPOHcuvrsVUalSmWh2hCHbyhv4'


class TweetFetcher(object):
    def __init__(self, query, max_tweets=50):
        self.GUID = 0
        self.query_terms = query.split(' ')
        self.count = 0
        self.MAX_TWEETS = max_tweets
        self.tso = TwitterSearchOrder()
        self.tso.setKeywords(self.query_terms)
        self.tso.setLanguage('en')
        self.tweets_per_page = 50
        self.tso.setCount(self.tweets_per_page)
        self.tso.setIncludeEntities(False)
        self.twitter_search = TwitterSearch(consumer_key, consumer_secret, access_token, access_token_secret)

    def get_tweets(self):
        output = []
        try:
            for tweet in self.twitter_search.searchTweetsIterable(self.tso):
                self.GUID += 1
                if self.GUID > self.MAX_TWEETS:
                    break
                output.append({'guid': self.GUID, 'id': tweet['id'], 'text': tweet['text'], 'query': self.query_terms})

        except TwitterSearchException as e:
            print e

        print len(output)
        return output


def get_slice(list_in, count):
    output = []
    for i in range(count):
        if len(list_in) > 0:
            output.append(list_in.pop())

    return output


class TweetStore(object):
    def __init__(self, query):
        self._classified_tweets = []
        self._objective_tweets = []
        self._tweet_fetcher = TweetFetcher(query)
        self.query = query
        self._unclassified_tweets = self._tweet_fetcher.get_tweets()

    def classify_batch(self):
        tweets = get_slice(self._unclassified_tweets, 10)
        for tweet in tweets:
            if tweet_contains_sentiment(tweet['text']):
                sentiment = classify_tweet(tweet['text'], tweet['query'])
                tweet['contains_sentiment'] = True
                tweet['sentiment'] = sentiment
                self._classified_tweets.append(tweet)
            else:
                tweet['contains_sentiment'] = False
                self._objective_tweets.append(tweet)
                print "OBJECTIVE TWEET " + tweet['text']

    def tweets_remain(self):
        if len(self._unclassified_tweets) > 0:
            return True
        else:
            return False

    def get_latest_tweets(self, start):
        return self._classified_tweets[start:]


class TweetProcessor(threading.Thread):

    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, verbose=None):
        super(TweetProcessor, self).__init__(group, target, name, args, kwargs, verbose)
        self.work_queue = Queue()
        self.daemon = True

    def addJob(self,store):
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
