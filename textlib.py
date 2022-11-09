"""
Example code from _Discovering Computer Science_, section 6.1
Author: Jessen Havill AND YOU
"""

import string

def removePunctuation(text):
    """Remove punctuation from a text.
    
    Parameter: text, a string object
    Return value: a copy of text with punctuation removed
    """
    text = text
    newText = ''
    for character in text:
        if character not in string.punctuation:
            newText = newText + character
    return newText

def normalize(text):
    """Normalize a text by making it lowercase and removing punctuation.

    Parameter: text, a string object
    Return value: a normalized copy of text
    """
    return removePunctuation(text.lower())

def splitIntoWords(text):
    """Split a text into words.

    Parameter: text, a string object
    Return value: the list of words in the text
    """
    return split(text, string.whitespace)

def split(text, splitChar):
    
    wordList = []
    prevCharacter = ' '
    word = ''
    for character in text:
        if character not in splitChar:
            word = word + character
        elif prevCharacter not in splitChar:
            wordList.append(word)
            word = ''
        prevCharacter = character

    if word != '':
        wordList.append(word)

    return wordList

def wordTokens(text):
    """Break a text into words with punctuation removed.
    Parameter: text, a string object
    Return value: a list of word tokens
    """

    return splitIntoWords(normalize(text))

def wordCount(text):
    """Count the number of words in a string.

    Parameter: text, a string object
    Return value: the number of words in text
    """
    return len(wordTokens(text))

def syllableCount(word):
    count = 0
    prevChar = ""
    for char in word:
        if char in "aeiou" and prevChar not in "aeiou":
            count += 1
        prevChar = char
    if word.endswith("e"):
        count -= 1
    
    return count
    
    
def main():
    shortText = "This isn't long. But it'll do.\n Just a few sentences..."
    print(shortText)
    print(wordCount(shortText), "words")

if __name__ == '__main__':
    main()
