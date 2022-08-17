'''
Created on Aug. 17, 2022

@author: AsifMahmud
'''
def rotateString(self, s: str, goal: str) -> bool:
    sLength = len(s)
    goalLength = len(goal)
    if sLength != goalLength:
        return False
    for i in range(sLength):
        if s[i] == goal[0] and s[i:] + s[:i] == goal:
            return True
    return False