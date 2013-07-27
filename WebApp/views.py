import datetime
import json
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template

__author__ = 'Luke'


def main_page(request):
    return render(request, 'main_page.html')


def do_search(request):
    if 'q' in request.GET:
        return HttpResponse('tweets about ' + request.GET['q'])
    else:
        return main_page(request)


def return_json(request):
    request.g
    d = {'a': 123, 'b': 124}
    return  HttpResponse(json.dumps(d))



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






