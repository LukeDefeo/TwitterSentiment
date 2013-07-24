__author__ = 'Luke'


with open('/Users/Luke/foriegn_test.csv') as file:
    with open('/Users/Luke/foriegn_test2.csv','w+') as out:

        s = file.read()
        out.write(s)




