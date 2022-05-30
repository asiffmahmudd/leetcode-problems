'''
Created on May 28, 2022

@author: AsifMahmud
'''
def repeatedSubstringPattern(self, s: str) -> bool:
    s_len = len(s)
    print((s+s)[1:-1])
    for i in range(1, s_len+1//2):
        sub_s = s[:i]
        multiple = s_len//i
        if(sub_s*multiple == s):
            return True
    return False