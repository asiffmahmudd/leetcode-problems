'''
Created on Sep. 2, 2022

@author: AsifMahmud
'''
def largeGroupPositions(self, s: str) -> List[List[int]]:
    interval = []
    count = 1
    start = 0
    for i in range (1, len(s)):
        if s[i-1] == s[i]:
            count += 1
        else:
            if count >= 3:
                interval.append([start, i-1])
            count = 1
            start = i
    if count >= 3:
        interval.append([start, i])
    return interval