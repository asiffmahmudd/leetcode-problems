'''
Created on May 31, 2022

@author: AsifMahmud
'''
def licenseKeyFormatting(self, s: str, k: int) -> str:
    s = ''.join(s.split('-')).upper()
    result = ""
    while(s):
        start = len(s)-k
        if start < 0:
            start = 0
        result = s[start:] + '-' + result
        s = s[:-k]
    return result[:-1