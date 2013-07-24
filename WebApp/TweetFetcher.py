__author__ = 'Luke'
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

consumer_key="ZYaUAuc8zNPM0BL5HgdSSg"
consumer_secret="x0Xpf6d6P4nHN2GYl91XOK032ppjhCYOIQCQQT9wA"

access_token="289934046-1sJjC4Oz1OGT3LYnKgoLGRUehicilfgzMR4TrS6v"
access_token_secret="qlulCQHYvEKBQFyPOHcuvrsVUalSmWh2hCHbyhv4"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# If the authentication was successful, you should
# see the name of the account print out
print api.me().name

# If the application settings are set for "Read and Write" then
# this line should tweet out the message to your account's
# timeline. The "Read and Write" setting is on https://dev.twitter.com/apps

class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """
    tweets = []
    count = 0

    def on_data(self, data):
        if len(self.tweets) < 50:
            self.tweets.append(data)
            return True
        else:
            return False

    def on_error(self, status):
        print status




l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

stream = Stream(auth, l)
stream.filter(track=['basketball'])

i = 1
for tweet in l.tweets:
    print 'tweet ' + str(i)
    i += 1
    print tweet


