'''
Created on Sep. 1, 2022

@author: AsifMahmud
'''
def toGoatLatin(self, sentence: str) -> str:
    wordCount = 0
    result = ""
    for word in sentence.split():
        if wordCount != 0:
            result += " "
        wordCount += 1
        if word[0] not in ("aeiouAEIOU"):
            word = word[1:len(word)] + word[0] 
        word += "ma" + "a" * wordCount
        result += word
    return result