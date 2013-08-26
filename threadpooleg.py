import threading
from threadpool import ThreadPool, makeRequests, WorkRequest
from TweetFetcher import TweetStore
import Queue
__author__ = 'Luke'

queue = Queue.Queue()
a = TweetStore('mircosoft')
b = TweetStore('sony')

queue.put(a)
queue.put(b)

class ThreadProcessor(threading.Thread):

    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, verbose=None):
        super(ThreadProcessor, self).__init__(group, target, name, args, kwargs, verbose)
        self.work_queue = Queue.Queue()
        self.daemon = True

    def run(self):
        super(ThreadProcessor, self).run()
        while True:
            print 'starting'
            store = self.work_queue.get()
            print 'geting from queue' + store.query
            store.classify_batch()
            if store.tweets_remain():
                self.work_queue.put(store)
                print 'putting back in queue'
            else:
                print 'done classifying' + store.query




def thread_run():
    while True:
        print 'starting'
        store = queue.get()
        print 'geting from queue'
        store.classify_batch()
        if store.tweets_remain():
            queue.put(store)
            print 'putting back in queue'
        else:
            print 'done classifying'



thread = threading.Thread(target=thread_run)
thread.setDaemon(False)
thread.start()

sessions = {'microsoft': a, 'sony': b}
# pool = ThreadPool(1)
#
# def put_in_queue(tweet_store):
#     pool.putRequest(WorkRequest(tweet_store.classify_batch))
#
# put_in_queue(a)
# print 'a in queue'
# put_in_queue(b)
# print 'b in queue'
#
# pool.wait()