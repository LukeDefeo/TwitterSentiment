from collections import OrderedDict

__author__ = 'Luke'


dic = OrderedDict()
dic['a'] = 1
dic['b'] = 2
dic['c'] = 3
dic['d'] = 4
dic['e'] = 5
dic['f'] = 6
dic['g'] = 7

def printdic(d):
    for key,val in d.items():
        print key + " " + str(val)

    print " "

print dic.keys()
dic.popitem(last=False)
print dic.keys()

printdic(dic)
printdic(dic)
# print dic.keys()
keys = dic.keys()
to_cull = keys[:int(0.5*len(keys))]
for key in to_cull:
    dic.pop(key)

printdic(dic)
