# -*- coding: utf-8 -*-
"""
Review and in-class exercises for section 7.3

Examples by Jessen Havill, _Discovering Computer Science 2/e_
Template by Janet Davis
Completed by ???
"""

import string

# Exercise 7.3.13  (modified)
def translateTxt(abbrv):
    """Translates text message abbreviations to English.

    Parameter:
        abbrv: a string object

    Return value: a string object corresponding to the given abbrv, 
                  or None if abbrv is not found
    """
    abbreviations = {'brb': 'be right back', 'omw': 'on my way', 'lol': 'laugh out loud'}
    return abbreviations.get(abbrv, "not in dictionary")
# Example p. 312 (will be modified to remove dependency on textlib)
def wordFrequencies(text):
    """Computes the frequencies of words in text.

    Parameter:
        text: a string object

    Return value: a dictionary containing word:count pairs
    """
    for punct in string.punctuation:
        text = text.replace(punct, '')
    wordList = text.lower().split()
    
    wordFreqs = {}
    
    for word in wordList:
        if word in wordFreqs:
            wordFreqs[word] = wordFreqs[word] + 1
        else:
            wordFreqs[word] = 1
            
    return wordFreqs

# Example p. 313-4 (modified)
def printFrequencies(frequencies, number):
    """Print an alphabetized table of keys and frequencies.

    Parameters:
        frequencies: a dictionary containing key:count pairs
        number: how many to print

    Return value: None
    """
    formatString = '{0:<20} {1:>5}'
    
    keyList = list(frequencies.keys())
    keyList.sort()
    
    
    print(formatString.format('Key', 'Frequency'))
    print(formatString.format('---', '---------'))
    for key in keyList[:number]:
        print(formatString.format(key, frequencies[key]))
        
# Exercise 7.3.5, p. 320
def firstLetterCounts(wordList):
    """Computes the frequencies of first letters in a list of words.

    Parameter:
        wordList: a list of string objects

    Return value: a dictionary containing letter:count pairs
    """
    
    frequencies = {}
    for word in wordList:
        firstLetter = word[0]
        if firstLetter in frequencies:
            frequencies[firstLetter] = frequencies[firstLetter] + 1
        else:
            frequencies[firstLetter] = 1
    
    return frequencies

# Exercise 7.3.6, p. 320
def firstLetterWords(wordList):
    """Grouop words by their first letter.

    Parameter:
        wordList: a list of string objects

    Return value: a dictionary containing letter:wordlist pairs
    """
    groups = {}
    
    for word in wordList:
        letter = word[0]
        if letter in groups:
            groups[letter].append(word)
        else:
            groups[letter] = [word]
    return groups

# Example p. 316
def mostFrequent(frequencies):
    """Find the key(s) with the highest frequency.

    Parameters:
        frequencies: a dictionary containing key:count pairs

    Return value: None
    """

# Example p. 316-7
def printMostFrequent(frequencies, limit=None):
    """Print a table of the highest frequency keys.

    Parameters:
        frequencies: a dictionary containing key:count pairs
        limit:       the maximum number of entries to print

    Return value: None
    """
    sortedValues = []
    for key in frequencies:
        sortedValues.append((frequencies[key], key))
    sortedValues.sort(reverse=True)
    
    formatString = '{0:<20} {1:>5}'
    
    print(formatString.format('Key', 'Frequency'))
    print(formatString.format('---', '---------'))
    for (freq, word) in sortedValues[:number]:
        print(formatString.format(word, freq))
        
        
# Example p. 319
def bigramFrequencies(text):
    """Find the frequencies of all bigrams in a text.

    Parameter:
        text: a string object

    Return value: a dictionary containing the bigram frequencies
    Bigrams are represented as pairs of string objects.
    """
     

