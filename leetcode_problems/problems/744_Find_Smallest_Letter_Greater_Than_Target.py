'''
Created on Jul. 28, 2022

@author: AsifMahmud
'''
def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    for letter in letters:
        if letter > target:
            return letter
    
    return letters[0]