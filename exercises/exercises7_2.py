# -*- coding: utf-8 -*-
"""
Review and in-class exercises for section 7.2

Examples by Jessen Havill, _Discovering Computer Science 2/e_
Template by Cary Gray
Completed by ???
"""

# Examples, pp. 294-297, 301-302

def mean(data):
    """Compute the mean of a non-empty list of numbers.

    Parameter:
        data: a list of numbers

    Return value: the mean of the numbers in data
    
    Uses built-in sum() function.
    """
    return sum(data) / len(data)

def smooth0(data, width):
    """Return a new list of data, smoothed over windows of given width.
    
    Parameters:
        data:  a list of numbers
        width: the widtn of each window
    
    Return value: a list of smoothed data values
    
    original version from p. 295
    """
    
    smoothedData = []
    
    for index in range(len(data)):
        window = data[index:index + width]
        smoothedData.append(mean(window))
    
    return smoothedData

def smooth(data, width):
    """Return a new list of data, smoothed over windows of given width.
    
    Parameters:
        data:  a list of numbers
        width: the widtn of each window
    
    Return value: a list of smoothed data values
    
    version from p. 296
    """
    
    smoothedData = []
    total = 0                                 # get sum for the first window
    for index in range(width):
        total = total + data[index]
    
    for index in range(len(data)):
        width = min(width, len(data) - index) # adjust the width near the end
        smoothedData.append(total / width)    # append the window mean
        total = total - data[index]           # subtract leftmost value
        if index + width < len(data):           # if possible
            total = total + data[index + width] #   add rightmost value
    
    return smoothedData

def smoothInPlace(data, width):
    """Smooth data in place over windows of given width.
    
    Parameters:
        data:  a list of numbers
        width: the widtn of each window
    
    Return value: None
    
    from pp. 301-302
    """
    total = 0                                 # get sum for the first window
    for index in range(width):
        total = total + data[index]
     
    for index in range(len(data)):
        width = min(width, len(data) - index) # adjust the width near the end
        mean = total / width                  # compute the window mean
        total = total - data[index]           # subtract leftmost value
        if index + width < len(data):           # if possible
            total = total + data(index + width) #   add rightmost value
    data[index] = mean                       # replace with window mean   


def squares(data):
    """Return a new list containing the squares of the elements of data.
    
    Parameters:
        data: a list of numbers
    
    Return value: a new list of squares
    """
    listSquares = []
    for i in data:
        listSquares = listSquares + [i**2]
    return listSquares
    
# 7.2.4
def square(data):
    """Replace each element of data with its square.
    
    Parameters:
        data: a list of numbers
    
    Return value: None
    """
    for i in range(len(data)):
        data[i] = data[i]**2
    return data
# 7.2.5
def swap(data, i, j):
    """Swap the elements at positions i and j in data.
    
    Parameters:
        data: a list
        i:    an index within data
        j:    an index within data
    
    Return value: None
    """
    iVal = data[i]
    data[i] = data[j]
    data[j] = iVal
    
    return data

# 7.2.6
def reverse(data):
    """Reverse list data in place.
    
    Parameters:
        data: a list
    
    Return value: None
    """
    for i in range(len(data)//2):
        swap(data, i, len(data) -i-1)
    return data





