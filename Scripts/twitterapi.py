from NLP.sentiment_analyser.sentiment_analyser import classify_tweet
from NLP.sentiment_detector.sentiment_detector import tweet_contains_sentiment

__author__ = 'Luke'
from tweepy.streaming import StreamListener, json
from tweepy import OAuthHandler
from tweepy import Stream


consumer_key = "ZYaUAuc8zNPM0BL5HgdSSg"
consumer_secret = "x0Xpf6d6P4nHN2GYl91XOK032ppjhCYOIQCQQT9wA"
access_token = "289934046-1sJjC4Oz1OGT3LYnKgoLGRUehicilfgzMR4TrS6v"
access_token_secret = "qlulCQHYvEKBQFyPOHcuvrsVUalSmWh2hCHbyhv4"

class TweetFetcher(StreamListener):
    def __init__(self, query, tweetstore, max_tweets=1000):
        super(TweetFetcher, self).__init__()
        self.tweet_store = tweetstore
        self._max_tweets = max_tweets
        self._query_terms = query.split()
        self._tweets = []
        self._count = 0
        self._alive = True
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        self._stream = Stream(auth, self)
        self._stream.filter(track=self._query_terms, async=True)

    def on_data(self, data):
        print data['text']
        if self._count < self._max_tweets and self._alive:
            tweet = json.loads(data)
            if tweet['lang'] == 'en':
                self.tweet_store.add_tweet(
                    {'guid': self._count, 'id': tweet['id'], 'text': tweet['text'], 'query': self._query_terms})

            self._count += 1
            return True
        else:
            print 'Reached tweet limit ... shutdown'
            return False

    def on_error(self, status):
        print 'Stream Error'
        print status


class TweetStore(object):
    def __init__(self, query):
        self._classified_tweets = []
        self._objective_tweets = []
        self._tweet_fetcher = TweetFetcher(query, self)
        self._query = query

    def get_tweets(self, start):
        return self._classified_tweets[start:]

    def add_tweet(self, tweet):
        if tweet_contains_sentiment(tweet['text']):

            sentiment = classify_tweet(tweet['text'], tweet['query'])
            tweet['contains_sentiment'] = True
            tweet['sentiment'] = sentiment
            self._classified_tweets.append(tweet)
        else:
            tweet['contains_sentiment'] = False
            self._objective_tweets.append(tweet)
            print "OBJECTIVE TWEET " + tweet['text']

    def shutdown(self):
        self._tweet_fetcher._alive = False

    def is_alive(self):
        return self._tweet_fetcher._alive
