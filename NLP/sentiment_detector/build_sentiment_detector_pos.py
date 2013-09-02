import cPickle as pickle
from sklearn import neighbors
from sklearn.svm import SVC
from NLP.sentiment_detector.sentiment_detector import extract_tags


__author__ = 'Luke'

source = pickle.load(open('../../Data/Training/sentiment_detector_training.obj'))
# extra = pickle.load(open('../../Data/Training/sentiment_detector_training-extra.obj'))

# source += extra
tagged_set, total_target = zip(*source)

total_data = [extract_tags(sent) for sent in tagged_set]
cut_off = int(0.85 * len(total_data))

training_data = total_data[:cut_off]
test_data = total_data[cut_off:]

training_target = total_target[:cut_off]
test_target = total_target[cut_off:]

svm = SVC()

svm.fit(training_data, training_target)

# pickle.dump(svm, open('../../Data/Models/sentiment-detector-knn','wb'))
print svm.score(test_data, test_target)