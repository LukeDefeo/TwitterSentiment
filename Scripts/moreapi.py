from TwitterSearch import *

__author__ = 'Luke'
# auth = tweepy.OAuthHandler('ZYaUAuc8zNPM0BL5HgdSSg', 'x0Xpf6d6P4nHN2GYl91XOK032ppjhCYOIQCQQT9wA')
access_token = "289934046-1sJjC4Oz1OGT3LYnKgoLGRUehicilfgzMR4TrS6v"
access_token_secret = "qlulCQHYvEKBQFyPOHcuvrsVUalSmWh2hCHbyhv4"
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth)




try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.setKeywords(['mircosoft']) # let's define all words we would like to have a look for
    tso.setLanguage('en') # we want to see German tweets only
    tso.setCount(7) # please dear Mr Twitter, only give us 7 results per page
    tso.setIncludeEntities(False) # and don't give us all those entity information
    ts = TwitterSearch(
        consumer_key = 'ZYaUAuc8zNPM0BL5HgdSSg',
        consumer_secret = 'x0Xpf6d6P4nHN2GYl91XOK032ppjhCYOIQCQQT9wA',
        access_token = '289934046-1sJjC4Oz1OGT3LYnKgoLGRUehicilfgzMR4TrS6v',
        access_token_secret = 'qlulCQHYvEKBQFyPOHcuvrsVUalSmWh2hCHbyhv4'
    )
    i=1
    for tweet in ts.searchTweetsIterable(tso):
        print i
        i +=1
        print('@%s tweeted: %s' % (tweet['user']['screen_name'], tweet['text']))


except TwitterSearchException as e:
    print e