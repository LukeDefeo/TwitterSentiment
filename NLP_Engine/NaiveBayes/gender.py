__author__ = 'Luke'
from nltk import NaiveBayesClassifier
from nltk.corpus import names
import nltk
import random


#Define a function to extract  features from data, these are just key value pairs,
#the value is important and is what the classifyer uses
def gender_features(word):
    return {'last_letter': word[-1],'first_letter' : word[0],'length' : len(word),'last_two' : word[len(word) - 2:],'last_three' : word[len(word) - 3:],'first_two' : word[:2]}

#Get data
names = ([(name, 'male') for name in names.words('male.txt')]) + \
        ([(name, 'female') for name in names.words('female.txt')])

random.shuffle(names)

#Define a feature set which is a set of tuples of gender features (last letter of name) and correct labels
feature_set = [(gender_features(name), gender) for (name, gender) in names]

#Split into test and training data
cut_off = int(0.8 * len(feature_set))
training_data = feature_set[:cut_off]
test_data = feature_set[cut_off:]

classifier = NaiveBayesClassifier.train(training_data)
a= classifier.prob_classify(test_data[0][0])
print test_data[0][0]
print nltk.classify.accuracy(classifier,test_data)
#print classifier.show_most_informative_features(100)



