import numpy as np

punctuationChr = [44,46,39,33,63,
                  59,58,34,125,45,
                  8221,8220,8230,123,92,
                  32,47,38]

punctuationStr = [chr(44),chr(46),chr(39),chr(33),chr(63),
                  chr(59),chr(58),chr(34),chr(125),chr(45),
                  chr(8221),chr(8220),chr(8230),chr(123),chr(92),
                  chr(32),chr(47),chr(38)]

def scriptParser(wordList2D):
    # First flatten the 2D word list
    wordList = [i for j in wordList2D for i in j]
    
    # Checks if the provided character is in the list of banned characters
    def charBanned(character):
        for i in range(len(punctuationChr)):
            if(ord(character) == punctuationChr[i]):
                return True
        return False
    
    # TODO: Implement deconcatination
    
    # Removes all spaces and punctuation
    def processText(text):
        newText = ""
        for i in range(len(text)):
            if(charBanned(text[i]) == False):
                newText = newText + text[i]
        return newText.lower()
    
    # Process all words to remove any strange grammar
    wordListProcessed = []
    for i in wordList:
        word = processText(i)
        if len(word) > 0:
            wordListProcessed.append(word)
        
    # Next convert all words to proper strings
    # This might not be needed tbh
    wordListString = []
    for i in wordListProcessed:
        wordListString.append(str(i))
        
    return wordListString
        