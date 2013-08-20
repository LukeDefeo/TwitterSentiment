import json
import pickle
import time
from tweepy import Stream, OAuthHandler, StreamListener
import tweepy
#this sc
__author__ = 'Luke'
auth = tweepy.OAuthHandler('ZYaUAuc8zNPM0BL5HgdSSg', 'x0Xpf6d6P4nHN2GYl91XOK032ppjhCYOIQCQQT9wA')
access_token = "289934046-1sJjC4Oz1OGT3LYnKgoLGRUehicilfgzMR4TrS6v"
access_token_secret = "qlulCQHYvEKBQFyPOHcuvrsVUalSmWh2hCHbyhv4"
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweets = []
start_time = time.time()
users = ['nytimes', 'UberFacts', 'Independent', 'World_CelebNews']
for user in users:
    print user
    for page in range(1, 17):
        timeline = api.user_timeline(user, count=200, page=page)
        for tweet in timeline:
            tweets.append(tweet.text)
        print page

        print len(timeline)

print len(tweets)
pickle.dump(tweets, open("../Data/Training/objective-tweets.obj", "wb"))
time_taken =   time.time() - start_time
print "took" + str(time_taken) + "secs"

