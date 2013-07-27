__author__ = 'Luke'
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time

consumer_key = "ZYaUAuc8zNPM0BL5HgdSSg"
consumer_secret = "x0Xpf6d6P4nHN2GYl91XOK032ppjhCYOIQCQQT9wA"

access_token = "289934046-1sJjC4Oz1OGT3LYnKgoLGRUehicilfgzMR4TrS6v"
access_token_secret = "qlulCQHYvEKBQFyPOHcuvrsVUalSmWh2hCHbyhv4"


class TweetFetcher(StreamListener):
    def __init__(self, query, no_tweets=100):
        super(TweetFetcher, self).__init__()
        self._count = no_tweets
        self._query_terms = query.split()
        self._tweets = []
        self._alive = True
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        self._stream = Stream(auth, self, timeout=10)
        self._stream.filter(track=self._query_terms, async=True)

    def get_latest_tweets(self,amount = 5):
        out = []
        for i in range(amount):
            if self._tweets:
                out.append(self._tweets.pop(-1))
        return out

    def shutdown(self):
        self._alive = False

    def on_data(self, data):
        if len(self._tweets) < self._count and self._alive:

            self._tweets.append(data)
            return True
        else:
            print 'Reached tweet limit ... shutdown'
            return False

    def on_error(self, status):
        print 'Stream Error'
        print status


fetcher = TweetFetcher( 'pokemon',15)
print '1'
time.sleep(10)
for data in fetcher.get_latest_tweets():
    print 'blah'
    print data

print 'set 1'

for data in fetcher.get_latest_tweets():
    print 'dattt'
    print data

fetcher.shutdown()