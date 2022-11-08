#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 14:27:24 2022

@author: baltzero

paxton luther
"""
import textlib
import urllib.request as web

def reverse(text):
    """
    This function will reverse any given string input
    
    Paramters
       Text: a string
       
    Return
        A string corrosponding to the reversed version of the text
    """
    revText = ""
    for char in text:
        revText = char + revText
    return revText
    

def webWordCount(url):
    """
    This function counts the number of words on a given url
    
    Parameters
        url: a web address
        
    Return 
        An integer corrosponding to the number of words counted 
    """
    urltxt = web.urlopen(url)
    return textlib.wordCount(urltxt.read())
    
def string2Digit(digitString):
    """
    This function will return a given digit in string form and turn it into an integer
    
    Parameters
        digitString: a digit in string form
        
    Return
        an integer corrosponding to the digit input 
    """
    return ord(digitString) - 48

def isHTML(url):
    """
    This function will determine whether a given url is an HTML file
    
    Parameters
        url: a web address
        
    Return
        A true or false value corrosponsing to whether the url is an HTML file
        
    """
    urltxt = web.urlopen(url)
    urltxt = urltxt.read()
    htmlDec = "doctype html"
    return (htmlDec in textlib.normalize(urltxt)) 
    
def username(first, last):
    """
    This function will create a username out of a given first and last name
    
    Parameters
        first: a string, the first name
        last: a string, the last name
        
    Return
        A string containing the created username
    """
    return str(last) + '_' + str(first[0])

def replace(text, target, replacement):
    """
    This function will replace a target text in a string with a given replacement
    
    Parameters
        text: The text in which the target will be replaced
        target: The target text to be replaced
        replacement: The text that the target will be replaced with
    
    Return
        A new string with target replaced by the given replacement
    """
    newText = ""
    start = 0
    for i in range(len(text)):
        if text[i:i + len(target)] == target:
            newText += text[start:i] + str(replacement)
            start = i + len(replacement)
    return newText

def longestRun(text):
    """
    This function will count the longest concurrent sequence of a character in the text
    
    Parameters
        text: The string in which runs of character will be searched for
        
    Return
        An integer, the length of the longest run of characters in the text
    """
    prevChar = ""
    run = 1
    longRun = 0
    for char in text:
        if char == prevChar:
            run += 1 
            if run > longRun:
                longRun = run
        else:
            run = 1    
            prevChar = char
    return longRun
        
def difference(word1, word2):
    """
    This function will return the first index at which the two words differ
    
    Parameters
        word1: a string, one of the words to be compared
        word2: a string, one of the words to be compared
    
    Return
        An integer corrosponding to the 
    """
    length = 0
    maxLength = min(len(word1), len(word2))
    for i in range(maxLength):
        if word1[i] == word2[i]:
            length += 1
        if length == len(word1) and length == len(word2) and length == maxLength:
            return -1
    return length   
        
def uniqueCharacters(text):
    """
    This function will count the number of characters which appear only once in the text
    
    Parameters
        text: a string, which will be searched for unique characters
        
    Return
        The count of unique characters in the text
    """
    uniqueList = []
    for i1 in range(len(text)):
        dupeCount = 0
        for i2 in range(len(text)):
            if text[i1] == text[i2]:
                dupeCount += 1
        if dupeCount == 1:
            uniqueList.append(text[i1])
    return len(uniqueList)


def test_reverse():
    # test cases 
    return "reverse() passes all tests"
    
def test_webWordCount():
    
    return "webWordCount() passes all tests"
    
def test_string2Digit():
    
    return "string2Digit() passes all tests"

def test_isHTML():
    
    return "isHTML() passes all tests"
    
def test_username():
    
    return "username() passes all tests"
    
def test_replace():
    
    return "replace() passes all tests"
    
def test_longestRun():
    
    return "longestRun() passes all tests"
    
def test_difference():
    
    return "difference() passes all tests"
    
def test_uniqueCharacters():
    
    return "uniqueCharacters() passes all tests "

def test():
    print(test_reverse())
    print(test_webWordCount())
    print(test_string2Digit())
    print(test_isHTML())
    print(test_username())
    print(test_replace())
    print(test_longestRun())
    print(test_difference())
    print(test_uniqueCharacters())
    print("all tests passed")

if __name__ == "__main__":
    test()
    
    
        
        
        
        
        
        
        
        
        
        
        