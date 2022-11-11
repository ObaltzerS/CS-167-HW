# -*- coding: utf-8 -*-
"""
Review and in-class exercises for section 7.1

Examples by Jessen Havill, _Discovering Computer Science 2/e_
Template by Janet Davis
Completed by ???
"""

# Example, p. 287
def mean(data):
    """Compute the mean of a non-empty list of numbers.

    Parameter:
        data: a list of numbers

    Return value: the mean of the numbers in data
    """

# Exercise 7.1.9
def meanSquares(data):
    """Computes the mean of the squares of a list of numbers.

    Parameter:
        data: a list of numbers

    Return value: the mean of the squares, or None if data is empty
    """

# Exercise 7.1.10
def variance(data):
    """Computes the variance of a list of numbers

    Parameter: 
        data: a list of numbers

    Return value: the variance of data, computed as the mean of the squares 
                  minus the square of the mean, or None if data is empty.
    """
    # Hint: Do not write a for loop. Instead, call mean() and meanSquares().

# Example, p. 288 (as min)
def listMin(data):
    """Find the minimum value in a non-empty list of numbers.

    Parameter: 
        data: a list of numbers

    Return value: the minimum value in data
    """

# Exercise 7.1.11
def listMax(data):
    """Find the maximum value in a non-empty list of numbers.

    Parameter: 
        data: a list of numbers

    Return value: the maximum value in data, or None if data is empty
    """

# Example, p. 289 (as minDay)
def minIndex(data):
    """Find the index of the minimum value in a non-empty list of numbers.

    Parameter: 
        data: a list of numbers

    Return value: the index of the minimum value in data
    """

# Exercise 7.1.14
def maxIndex(data):
    """Finds the index of the maximum value in a non-empty list of numbers.

    Parameter: 
        data: a list of numbers

    Return value: the index of the maximum value in data
    """

# Example, p. 289-290
def weekday(index):
    """Name the day of the week corresponding to the given index: 
       0 for Sunday up to 6 for Saturday.

    Parameter:
        index, an integer between 0 and 6, inclusive

    Return value: a string representing the day of the week
    """
    if index == 0:
        return 'Sunday'
    if index == 1:
        return 'Monday'
    if index == 2:
        return 'Tuesday'
    if index == 3:
        return 'Wednesday'
    if index == 4:
        return 'Thursday'
    if index == 5:
        return 'Friday'
    if index == 6:
        return 'Saturday'
    assert False, 'index must be between 0 and 6, inclusive'
    
# Exercise 7.1.8
def percentile(data, value):
    """Computes the percentile of a value in a list.

    Parameters:
        data: a list of numbers
        value: the value to determine the percentile of

    Return value: the percentile of value in data. 

    The percentile associated with a particular value in a data set is the
    number of values less than or equal to it, divided by the total number 
    of values, times 100.
    """

# Exercise 7.1.17
def linearSearch(data, target):
    """Finds the index of a target value in a list of data.

    Parameters:
        data: a list
        target: a value to search for

    Return value: the index of target in data, or -1 if not found
    """

# Exercise 7.1.15
def secondLargest(data):
    """Finds the second largest number in data.

    Parameter:
        data, a list of numbers

    Return value: the second largest number in data
    """
    # Issue: What are the preconditions for this function?
    # Issue: What if the largest number appears twice?
    # Hint: Call the maxIndex function from exercise 7.1.15.

# If you still have more time, try any/all of exercises 7.1.(18-20).
