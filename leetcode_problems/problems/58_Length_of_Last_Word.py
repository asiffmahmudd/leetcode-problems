'''
Created on Dec 3, 2021

@author: AsifMahmud
'''
def lengthOfLastWord(self, s: str) -> int:
    words = s.split()
    return len(words[len(words)-1])