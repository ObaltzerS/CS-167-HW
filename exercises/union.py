#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Solution to exercise 7.3.16, p. 322

Created on Mon Nov 29 13:08:01 2021

@author: davisj
"""

def union(dict1, dict2):
    """Returns a dictionary that contains all the entries 
    of the two dictionaries dict1 and dict2. If they share
    a key, use the value in the first dictionary.
    """
    # More concise
    newDict = dict2.copy()
    for key in dict1:   
        newDict[key] = dict1[key]
    return newDict

    # More obviously correct
    newDict = {}
    for key in dict1:
        newDict[key] = dict1[key]
    for key in dict2:
        if key not in newDict:
            newDict[key] = dict2[key]
    return newDict




def test_union():
    assert union({}, {}) == {}
    assert union({'a':1}, {'b':2}) == {'a':1,'b':2}
    assert union({'a':1}, {'a':2, 'b':2}) == {'a':1,'b':2}
    print("All tests of union passed!")
    
test_union()    
    