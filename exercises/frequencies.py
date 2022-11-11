"""
Compute and display the frequencies of words and bigrams in a text.

Author: Jessen Havill
Source: _Discovering Computer Science_ 2/e, section 7.3 (p. 312, 319)
"""

import textlib

def wordFrequencies(text):
    """Given a text, returns a dictionary of word:count pairs."""

    wordList = textlib.wordTokens(text)
    wordFreqs = {}
    for word in wordList:
        if word in wordFreqs:
            wordFreqs[word] = wordFreqs[word] + 1
        else:
            wordFreqs[word] = 1
    return wordFreqs

def bigramFrequencies(text):
    """Given a text, returns a dictionary of (first,second):count pairs."""

    wordList = textlib.wordTokens(text)
    bigramFreqs = {}
    prevWord = wordList[0]
    for word in wordList[1:]:
        bigram = (prevWord, word)
        if bigram in bigramFreqs:
            bigramFreqs[bigram] = bigramFreqs[bigram] + 1
        else:
            bigramFreqs[bigram] = 1
        prevWord = word
    return bigramFreqs

def printMostFrequent(frequencies, number):
    """Prints an ordered table of keys and frequencies.
    
    Parameters:
        frequencies: a dictionary containing key:count pairs
        number:      the number of entries to print

    Return value: none
    """

    sortedValues = []
    for key in frequencies:
        sortedValues.append((frequencies[key], key))
    sortedValues.sort(reverse=True)

    print('{0:<20} {1}'.format('Key', 'Frequency'))
    print('{0:<20} {1}'.format('---', '---------'))
    for pair in sortedValues[:number]:
        key = pair[1]
        print('{0:<20} {1:>9}'.format(str(key), frequencies[key]))

def main():
    filename = 'frankenstein.txt'
    text = open(filename, 'r').read()
    print()
    print('File: {}'.format(filename))

    wordfreq = wordFrequencies(text)
    print()
    print()
    print('Most common words out of {}'.format(len(wordfreq)))
    print()
    printMostFrequent(wordfreq, 10)

    bigramfreq = bigramFrequencies(text)
    print()
    print()
    print('Most common bigrams out of {}'.format(len(bigramfreq)))
    print()
    printMostFrequent(bigramfreq, 10)

if __name__ == '__main__':
    main()
