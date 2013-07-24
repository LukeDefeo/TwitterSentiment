import datetime
import json
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template

__author__ = 'Luke'


def main_page(request):
    return render(request,'main_page.html')


def do_search(request):
    if 'q' in request.GET:
        return HttpResponse('tweets about ' + request.GET['q'])
    else:
        return main_page(request)


def hello(request):
    return HttpResponse("hello World!!!!")


def current_datetime(request):
    now = datetime.datetime.now()
    template = get_template('current_datetime.html')
    html = template._render(Context({'current_date': now}))
    return HttpResponse(html)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)


def test_json(request, query):
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=[query])

    return HttpResponse(json.dumps(l.tweets))


import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

consumer_key = "ZYaUAuc8zNPM0BL5HgdSSg"
consumer_secret = "x0Xpf6d6P4nHN2GYl91XOK032ppjhCYOIQCQQT9wA"

access_token = "289934046-1sJjC4Oz1OGT3LYnKgoLGRUehicilfgzMR4TrS6v"
access_token_secret = "qlulCQHYvEKBQFyPOHcuvrsVUalSmWh2hCHbyhv4"

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
        if len(self.tweets) < 7:
            self.tweets.append(data)
            return True
        else:
            return False

    def on_error(self, status):
        print status






