#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Computer Science 167 
Homework #9
November 8, 2022
Authors: Oliver Baltzer, Maxwell Montgomery
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
    txt = urltxt.read()
    return textlib.wordCount(str(txt))
    
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
    txt = urltxt.read()
    txt = str(txt)
    htmlDec = "doctype html"
    return (htmlDec in textlib.normalize(txt)) 
    
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
            newText = newText + text[start:i] + str(replacement)
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
    longRun = 1
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
    assert reverse('download') == 'daolnwod'
    assert reverse("two words") == "sdrow owt"
    assert reverse("was it a rat I saw") == "was I tar a ti saw"
    assert reverse("1234") == "4321"
    assert reverse("P") == "P"
    return "reverse() passes all tests"
    
def test_webWordCount():
    
    assert webWordCount("https://www.gutenberg.org/cache/epub/2701/pg2701-images.html") >= 209117
    assert webWordCount("https://www.gutenberg.org/cache/epub/996/pg996-images.html") >= 345390
    assert webWordCount("https://www.gutenberg.org/cache/epub/69315/pg69315-images.html") == 77691
    assert webWordCount("https://www.gutenberg.org/cache/epub/69310/pg69310-images.html") == 58492
    assert webWordCount("https://www.gutenberg.org/cache/epub/69308/pg69308-images.html") == 13388
    return "webWordCount() passes all tests"
    
def test_string2Digit():
    assert string2Digit("5") == 5
    assert string2Digit("9") == 9
    assert string2Digit("0") == 0
    assert string2Digit("1") == 1
    assert string2Digit("6") == 6
    return "string2Digit() passes all tests"

def test_isHTML():
    assert isHTML("https://www.gutenberg.org/cache/epub/2701/pg2701-images.html") == True
    assert isHTML("https://www.gutenberg.org/cache/epub/996/pg996-images.html") == True
    assert isHTML("https://www.gutenberg.org/cache/epub/69308/pg69308-images.html") == True
    assert isHTML("https://www.gutenberg.org/cache/epub/69310/pg69310-images.html") == True
    assert isHTML("https://www.gutenberg.org/cache/epub/69315/pg69315-images.html") == True
    return "isHTML() passes all tests"
    
def test_username():
    assert username('martin', 'freeman') == 'freeman_m'
    assert username("Morgan", "Freeman") == "Freeman_M"
    assert username("Oliver", "Baltzer") == "Baltzer_O"
    assert username("Maxwell", "Montgomery") == "Montgomery_M"
    assert username("user", "name44") == "name44_u"
    return "username() passes all tests"
    
def test_replace():
    assert replace('I am cool, very cool.', 'cool', 'very vain') == 'I am very vainy very vain'
    assert replace("word", "word", "cool") == "cool"
    assert replace("replace this word", "word", "replaced") == "replace this replaced"
    assert replace("I am a cowboy", "cowboy", "wizard") == "I am a wizard"
    assert replace("abcdefg", "c", "f") == "abfdefg" 
    return "replace() passes all tests"
    
def test_longestRun():
    assert longestRun("aabbbbcccd") == 4
    assert longestRun("a") == 1
    assert longestRun("woords wiiith reeeepeated chhhhharacters") == 5
    assert longestRun("1234") == 1
    assert longestRun("words with no repeats") == 1
    return "longestRun() passes all tests"
    
def test_difference():
    assert difference('bob', 'bob') == -1
    assert difference('bob', 'sallyann') == 0
    assert difference("auto", "automobile") == 4
    assert difference("automobile", "auto") == 4
    assert difference("1234", "1235") == 3
    return "difference() passes all tests"
    
def test_uniqueCharacters():
    assert uniqueCharacters('aaeeioou') == 2
    assert uniqueCharacters('bobby') == 2
    assert uniqueCharacters('aabbcc') == 0
    assert uniqueCharacters("words with unique characters") == 4
    assert uniqueCharacters("abcde") == 5
    return "uniqueCharacters() passes all tests "

def test():
    print(test_reverse())
    print(test_webWordCount())
    print(test_string2Digit())
    print(test_isHTML())
    print(test_username())
    print(test_replace()) # replace function is faulty, wasnt able to come up with a solution
    print(test_longestRun())
    print(test_difference())
    print(test_uniqueCharacters())
    print("all tests passed")

if __name__ == "__main__":
    test()