#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess

from sklearn.svm import SVC


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

# 减小数据集
# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]


clf = SVC(C=10000.0,kernel='rbf')

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

print clf.score(features_test, labels_test)

predictions = clf.predict(features_test)

print "Predctions:"

print len(predictions[predictions==1])
