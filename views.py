import datetime
import time
import json
import django
from django.http import HttpResponse, Http404, HttpResponseBadRequest
from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template
from TweetFetcher import TweetStore

__author__ = 'Luke'

__sessions = {}


def main_page(request):
    return render(request, 'main_page.html')


def do_search(request):
    if 'q' in request.GET:
        return HttpResponse('tweets about ' + request.GET['q'])
    else:
        return main_page(request)


def return_json(request):
    query = request.GET .get('q', '')
    if query == '':
        return HttpResponseBadRequest()

    start = int(request.GET.get('start', 0))
    global __sessions

    if query not in __sessions:
        print 'creating new object for ' + query
        __sessions[query] = TweetStore(query)

    fetcher = __sessions[query]


    print 'start ='  + str(start)

    data = fetcher.get_latest_tweets(start)
    print data
    print 'Returning reponse'
    return HttpResponse(json.dumps(data, ensure_ascii=False))


# called internally
def clean_up(request):
    pass


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







