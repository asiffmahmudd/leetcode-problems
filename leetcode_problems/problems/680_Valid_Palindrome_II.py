'''
Created on Jul. 11, 2022

@author: AsifMahmud
'''
def validPalindrome(self, s: str) -> bool:
    def checkPalindrome(s, i, j):
        temp = s[i:j]
        if temp == temp[::-1]:
            return True
    i, j = 0, len(s)-1
    while i < j:
        if(s[i] != s[j]):
            return checkPalindrome(s, i+1, j+1) or checkPalindrome(s, i, j)
        i += 1
        j -= 1
    
    return True