#!/usr/bin/python
import numpy

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    quantity_to_remove = int(len(predictions) * 0.9)
    diff = (predictions - net_worths) ** 2
    new_diff = []
    for i in range(len(diff)):
        new_diff.append(diff[i][0])
    check_value = numpy.partition(new_diff, quantity_to_remove)[quantity_to_remove]

    new_age = []
    new_net = []
    new_error = []

    for i in range(len(ages)):
        if new_diff[i] < check_value:
            new_age.append(ages[i][0])
            new_net.append(net_worths[i][0])
            new_error.append(diff[i][0])
    print "old length:", len(ages)
    print "new length:", len(new_age)
    cleaned_data = zip(new_age, new_net, new_error)

    return cleaned_data
