#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

    ['salary', 'to_messages', 'deferral_payments', 'total_payments',
    'exercised_stock_options', 'bonus', 'restricted_stock',
    'shared_receipt_with_poi', 'restricted_stock_deferred', 'total_stock_value',
    'expenses', 'loan_advances', 'from_messages', 'other',
    'from_this_person_to_poi', 'poi', 'director_fees', 'deferred_income',
    'long_term_incentive', 'email_address', 'from_poi_to_this_person']

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

'''
count = 0

for person in enron_data:
    if enron_data[person]["poi"] == 1:
        count += 1

print count

print enron_data["PRENTICE JAMES"]

print enron_data["COLWELL WESLEY"]['from_this_person_to_poi']



for person in enron_data:
    if person.find("SKILLING") >=0 :
        print "name:{}, total payments: {}".format(person, enron_data[person]['total_payments'])


CEO : Jeffrey Skilling => SKILLING JEFFREY K
chairman : Kenneth Lay => LAY KENNETH L
CFO : Andrew Fastow => FASTOW ANDREW S
'''

'''
quantified_salary = 0
known_email = 0

for person in enron_data:
    if enron_data[person]["salary"] != "NaN":
        quantified_salary += 1

    if enron_data[person]["email_address"] != "NaN":
        known_email +=1

print "quantified salary :{} \nknow email: {}".format(quantified_salary, known_email)
'''

non_total_payments = 0
for person in enron_data:
    if enron_data[person]["total_payments"] == "NaN":
        non_total_payments += 1

print non_total_payments * 1.0 / 146.0

non_salary = 0
for person in enron_data:
    if enron_data[person]["salary"] == "NaN":
        non_total_payments += 1

print non_salary * 1.0 / 146.0

print non_total_payments
