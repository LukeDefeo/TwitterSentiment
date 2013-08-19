import cPickle as pickle
import random
from sklearn.svm import SVC

__author__ = 'Luke'
import numpy
from sklearn import datasets, neighbors


iris = datasets.load_iris()
knn = neighbors.KNeighborsClassifier(algorithm='auto',
                                     leaf_size=30, n_neighbors=5)
perm = numpy.random.permutation(iris.target.size)

feature_set = pickle.load(open("../../Data/Training/tagged-sents.obj"))
print feature_set




train = []
with open(
        '/Users/Luke/Dropbox/Comp Sci/Intelligent Data Analysis/Assignment/boston/BOSTON.EX/data.no_price.norm.dat') as inputs:
    for line in inputs:
        values = [float(value[:-4]) for value in line.split()]
        train.append(values)

targets = []
with open(
        '/Users/Luke/Dropbox/Comp Sci/Intelligent Data Analysis/Assignment/boston/BOSTON.EX/data.no_price.norm.dat') as target:
    for line in target:
        targets.append(int(line[3]))

cutoff = int(0.85 * len(targets))
knn.fit(train[:cutoff], targets[:cutoff])
print knn.score(train[cutoff:], targets[cutoff:])

clf = SVC()
clf.fit(train[:cutoff], targets[:cutoff])
print clf.score(train[cutoff:], targets[cutoff:])
#
# iris.data = iris.data[perm]
# iris.target = iris.target[perm]
# knn.fit(iris.data[:100], iris.target[:100])
# print knn.score(iris.data[100:], iris.target[100:])
