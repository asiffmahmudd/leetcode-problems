'''
Created on May 22, 2022

@author: AsifMahmud
'''
def longestPalindrome(self, s: str) -> int:
    str_dictionary = dict(Counter(s))
    singleFlag = True
    result = 0
    for val in str_dictionary.values():
        if(val%2 == 0):
            result += val
        elif (singleFlag and val%2 == 1):
            result += val
            singleFlag = False
        else:
            result += val-1
    return result