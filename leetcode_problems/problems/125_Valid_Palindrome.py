'''
Created on Dec 29, 2021

@author: AsifMahmud
'''
def isPalindrome(self, s: str) -> bool:
    s = s.lower()
    for c in s:
        if(c < 'a' or c > 'z') and (c < '0' or c > '9'):
            s = s.replace(c,'')
    
    temp = s[::-1]
    
    if temp == s:
        return True
    else:
        return False