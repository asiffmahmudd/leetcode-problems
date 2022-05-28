'''
Created on May 27, 2022

@author: AsifMahmud
'''
def findContentChildren(self, g: List[int], s: List[int]) -> int:
    s.sort()
    g.sort()
    
    i = 0
    j = 0
    s_len = len(s)
    g_len = len(g)
    count = 0
    
    while i < g_len and j < s_len:
        if g[i] <= s[j]:
            count += 1
            i += 1
        j += 1
        
    return count