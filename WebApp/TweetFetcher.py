__author__ = 'Luke'
from tweepy.streaming import StreamListener, json
from tweepy import OAuthHandler
from tweepy import Stream


def strip_tweet(tweet):
    pass


def tweet_contains_sentiment(tweet):
    return True


def process_sentiment(tweet):
    pass


# class TweetStore(object, query):
#     def __init__(self):
#         self._tweets = []
#         self._tweet_fetcher = TweetFetcher()
#
#     def get_tweets(self, start):
#         return self._tweets[start:]
#
#     def add_tweet(self, tweet):
#         if tweet_contains_sentiment(tweet):
#             process_sentiment(tweet)
#             strip_tweet(tweet)
#             self._tweets.append(tweet)
#
#     def is_alive(self):
#         return self._tweet_fetcher._alive


class TweetFetcher(StreamListener):
    consumer_key = "ZYaUAuc8zNPM0BL5HgdSSg"
    consumer_secret = "x0Xpf6d6P4nHN2GYl91XOK032ppjhCYOIQCQQT9wA"

    access_token = "289934046-1sJjC4Oz1OGT3LYnKgoLGRUehicilfgzMR4TrS6v"
    access_token_secret = "qlulCQHYvEKBQFyPOHcuvrsVUalSmWh2hCHbyhv4"

    def __init__(self, query, max_tweets=100, ):
        super(TweetFetcher, self).__init__()
        self._max_tweets = max_tweets
        self._query_terms = query.split()
        self._tweets = []
        self._count = 0
        self._alive = True
        auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)

        self._stream = Stream(auth, self)
        self._stream.filter(track=self._query_terms, async=True)

    def get_latest_tweets(self, amount=5):
        out = []
        for i in range(amount):
            if self._tweets:
                out.append(self._tweets.pop(-1))
        return out

    def get_tweets(self, start):
        return self._tweets[int(start):]

    def shutdown(self):
        self._alive = False

    def is_alive(self):
        return self._alive

    def on_data(self, data):
        if len(self._tweets) < self._max_tweets and self._alive:
            tweet = json.loads(data)
            if tweet['lang'] == 'en':
                self._tweets.append({'guid': len(self._tweets), 'id': tweet['id'], 'text': tweet['text'], })

            return True
        else:
            print 'Reached tweet limit ... shutdown'
            return False

    def on_error(self, status):
        print 'Stream Error'
        print status


        # def test():
        #     fetcher = TweetFetcher('pokemon', 15)
        #     print '1'
        #     time.sleep(10)
        #     for data in fetcher.get_latest_tweets():
        #         print 'blah'
        #         print data
        #
        #     print 'set 1'
        #
        #     for data in fetcher.get_latest_tweets():
        #         print 'dattt'
        #         print data
        #
        #     fetcher.shutdown()