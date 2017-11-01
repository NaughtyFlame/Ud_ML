#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)
'''
max_value = data.max(axis=0)

print max_value

for person in data_dict:
    if data_dict[person]["salary"] == max_value[0]:
        print person
        break
### your code below

data_dict.pop(person)
data = featureFormat(data_dict, features)
'''

for person in data_dict:
    if (data_dict[person]['bonus'] > 5000000 and data_dict[person]['bonus'] !="NaN" and
        data_dict[person]['salary'] > 1000000):
        print person
        print data_dict[person]['bonus']

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
