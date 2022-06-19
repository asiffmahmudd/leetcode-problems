'''
Created on Jun. 18, 2022

@author: AsifMahmud
'''
def checkRecord(self, s: str) -> bool:
    return True if "LLL" not in s and s.count('A') < 2 else False