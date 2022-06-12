'''
Created on Jun 11, 2022

@author: AsifMahmud
'''
def detectCapitalUse(self, word: str) -> bool:
    if word.isupper() or word.islower() or word[0].upper() + word[1:].lower() == word:
        return True
    return False