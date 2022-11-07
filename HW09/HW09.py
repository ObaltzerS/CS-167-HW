#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 14:27:24 2022

@author: baltzero

paxton luther
"""
import textlib
import urllib.request as web
import string

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
        
    """
    urltxt = web.urlopen(url)
    urltxt = urltxt.read()
    htmlDec = "doctype html"
    return (htmlDec in textlib.normalize(urltxt)) 
    
def username(first, last):
    return str(last) + '_' + str(first[0])

def replace(text, target, replacement):
    newText = ""
    start = 0
    for i in range(len(text)):
        if text[i:i + len(target)] == target:
            newText += text[start:i] + str(replacement)
            start = i + len(replacement)
    return newText

def longestRun(text):
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
    
    length = 0
    maxLength = min(len(word1), len(word2))
    for i in range(maxLength):
        if word1[i] == word2[i]:
            length += 1
        if length == len(word1) and length == len(word2) and length == maxLength:
            return -1
    return length   
        
def uniqueCharacters(text):
    uniqueList = []
    for i1 in range(len(text)):
        dupeCount = 0
        for i2 in range(len(text)):
            if text[i1] == text[i2]:
                dupeCount += 1
        if dupeCount == 1:
            uniqueList.append(text[i1])
    return len(uniqueList)
    
        
        
        
        
        
        
        
        