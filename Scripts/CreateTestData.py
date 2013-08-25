__author__ = 'Luke'


print 'start '

with open("/Users/Luke/Documents/Project-Files/Test-Data/testdata.manual.2009.06.14.csv") as input:
    with open("../Data/Test/test-data.csv",'w+') as output:
        for each_line in input:
            elements = each_line.split('","')
            elements[0] = elements[0][1:]
            elements[5] = elements[5][:-2]
            if(elements[0] == '0'):
                elements[0] = 'neg'
            if(elements[0] == '2'):
                continue
            if(elements[0] == '4'):
                elements[0] = 'pos'


            output.write(elements[0] + "\t" + elements[5] + '\n')




print 'done'