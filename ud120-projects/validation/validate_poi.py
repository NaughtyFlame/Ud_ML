#!/usr/bin/python


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn import tree
from sklearn.model_selection import train_test_split

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.

# fonctions

def accuracy_score(truth, pred):
    if len(truth) == len(pred):
        return "accuracy: {}".format((truth == pred).mean()*100)
    else:
        return "Number of predictions does not match number of outcomes!"

features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

features_train, features_test, labels_train, labels_test = train_test_split(
    features, labels, test_size=0.3, random_state=42)


clf = tree.DecisionTreeClassifier()
clf.fit(features_train, labels_train)

predictions = clf.predict(features_test)

print "POIs : {}".format(len(predictions[predictions == 1]))
print "Total People: {}".format(len(predictions))

# Q7 : true positive
print "True Positive: ",sum(predictions * labels_test)

# Q8 precision score
from sklearn.metrics import precision_score
print "precision score: ",precision_score(labels_test, predictions)

# Q9 recall score
from sklearn.metrics import recall_score
print "recall score: ", recall_score(labels_test, predictions)

# print "score: {}".format(clf.score(features_test, labels_test))
