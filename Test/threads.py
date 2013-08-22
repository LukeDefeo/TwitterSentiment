import threading
import time
import thread

__author__ = 'Luke'





def function():
    print 'inside'
    print threading.currentThread().name
    time.sleep(3)
    print 'outside'


t1 = threading.Thread(target=function)
t2 = threading.Thread(target=function)

t1.start()
t2.start()