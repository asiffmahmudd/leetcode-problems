'''
Created on Jun. 15, 2022

@author: AsifMahmud
'''
def findLUSlength(self, a: str, b: str) -> int:
    return -1 if a == b else len(a) if len(a) > len(b) else len(b)