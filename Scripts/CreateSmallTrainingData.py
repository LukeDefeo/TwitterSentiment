__author__ = 'Luke'


import os

__author__ = 'Luke'

print 'start '
counter = 0
with open("/Users/Luke/Documents/Project-Files/Training-Data/training.1600000.processed.noemoticon.csv") as input:
    with open("/Users/Luke/Documents/PyCharmProjects/TwitterSentiment/Data/Training/training-data-small.csv",'w') as output:
        for each_line in input:
            elements = each_line.split('","')
            elements[0] = elements[0][1:]
            elements[5] = elements[5][:-2]
            if(elements[0] == '0'):
                elements[0] = 'neg'
            if(elements[0] == '2'):
                elements[0] = 'neutral'
            if(elements[0] == '4'):
                elements[0] = 'pos'

            if counter % 10 == 0:
                output.write(elements[0] + "\t" + elements[5] + '\n')

            counter += 1



print 'done'