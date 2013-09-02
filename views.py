from collections import OrderedDict
import datetime
import time
import json
import django
from django.http import HttpResponse, Http404, HttpResponseBadRequest
from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template
from TweetFetcher import TweetStore, TweetProcessor

__author__ = 'Luke'

local_cache = OrderedDict()
processor = TweetProcessor()
processor.start()


def main_page(request):
    return render(request, 'main_page.html')


def return_json(request):
    global local_cache
    query = request.GET.get('q', '')
    print query
    if query == '':
        return HttpResponseBadRequest()
    start = int(request.GET.get('start', 0))

    if query not in local_cache:
        store = TweetStore(query)
        local_cache[query] = store
        processor.addJob(store)
        time.sleep(3)

    tweet_store = local_cache[query]
    print 'start =' + str(start)
    data = tweet_store.get_latest_tweets_all(start)
    return HttpResponse(json.dumps(data, ensure_ascii=False))


# called internally
def clean_up(request):
    print 'Beginning cleanup, killing 10% of cache'
    print 'Before'
    print local_cache.keys()
    to_kill = int(0.1 * len(OrderedDict))
    for i in xrange(to_kill):
        local_cache.popitem(last=False)

    print 'After'
    print local_cache.keys()


