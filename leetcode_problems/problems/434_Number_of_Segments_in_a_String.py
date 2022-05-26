'''
Created on May 25, 2022

@author: AsifMahmud
'''
def countSegments(self, s: str) -> int:
    # return len(s.split())
    s = " ".join(s.split())
    if s:
        return len(s.split(" "))
    else:
        return 0