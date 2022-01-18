'''
Created on Jan 17, 2022

@author: AsifMahmud
'''

def wordPattern(self, pattern: str, s: str) -> bool:
    words = s.split(" ")
    dictionary = {}
    if len(words) != len(pattern):
        return False
    for letter, word in zip(pattern,words):
        if letter not in list(dictionary.values()):
            if word in list(dictionary.keys()):
                dictionary[word] = '-'
            else:
                dictionary[word] = letter
    result_string = ""
    
    for word in words:
        if word in list(dictionary.keys()):
            result_string += dictionary[word]
    return result_string == pattern