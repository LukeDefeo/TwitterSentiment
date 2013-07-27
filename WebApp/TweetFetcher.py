import threading
import time

__author__ = 'Luke'
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

consumer_key = "ZYaUAuc8zNPM0BL5HgdSSg"
consumer_secret = "x0Xpf6d6P4nHN2GYl91XOK032ppjhCYOIQCQQT9wA"

access_token = "289934046-1sJjC4Oz1OGT3LYnKgoLGRUehicilfgzMR4TrS6v"
access_token_secret = "qlulCQHYvEKBQFyPOHcuvrsVUalSmWh2hCHbyhv4"


class TweetFetcher(StreamListener):
    def __init__(self, no_tweets, query):
        super(TweetFetcher, self).__init__()
        self._count = no_tweets
        self._query_terms = query.split()
        self._tweets = []

        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        self._stream = Stream(auth, self, timeout=10)
        self._stream.filter(track=query.split())

    def get_latest_tweets(self):
        out = []
        for i in range(5):
            out.append(self._tweets.remove(-1))
        return out

    def set_search_query(self, query):
        self._stream.filter(track=query.split())

    def on_data(self, data):
        if len(self._tweets) < self._count:
            print data
            # print len(self._tweets)
            self._tweets.append(data)
            return True
        else:
            print 'Reached tweet limit over... shutdown'
            return False

    def on_error(self, status):
        print 'error'
        print status

    def on_timeout(self):
        print   'Timeout...'
        return True # Don't kill the stream


class TweetBuffer(object):
    pass


def start():
    pass


thread = threading.Thread(target=TweetFetcher, args=(10, 'basketball'))
thread.start()

print 'done this line'
time.sleep(2)
print 'changing topic'
# tweet_getter.set_search_query('justin bieber')



