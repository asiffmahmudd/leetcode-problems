'''
Created on Jun. 14, 2022

@author: AsifMahmud
'''
def reverseStr(self, s: str, k: int) -> str:
    len_s = len(s)
    if len_s < k:
        return s[::-1]
    
    start = 0
    end = k
    
    while start < len_s:
        s = s[:start] + s[start:end][::-1] + s[end:]
        start += 2*k
        end = start + k

    return s