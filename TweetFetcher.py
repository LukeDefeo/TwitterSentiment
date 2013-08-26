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
                print tweet['text']
                self.GUID += 1
                if self.GUID > self.MAX_TWEETS:
                    break
                output.append({'guid': self.GUID, 'id': tweet['id'], 'text': tweet['text'], 'query': self.query_terms})

        except TwitterSearchException as e:
            print e

        print len(output)
        return output


class TweetStore(object):
    def __init__(self, query):
        self._classified_tweets = []
        self._objective_tweets = []
        self._tweet_fetcher = TweetFetcher(query)
        self._query = query

    def classify_batch(self):
        tweets = self._tweet_fetcher.get_tweets()
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

    def get_latest_tweets(self, start):
        return self._classified_tweets[start:]

