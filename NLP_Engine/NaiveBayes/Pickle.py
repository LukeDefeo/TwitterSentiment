import pickle

__author__ = 'Luke'


a = set()
sent = "there are some words in this sentence pickle this"
for word in sent.split():
    a.add(word)


print pickle.dump(a,open("pickle.obj","wb"))