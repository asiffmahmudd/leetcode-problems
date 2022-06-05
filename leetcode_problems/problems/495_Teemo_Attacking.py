'''
Created on Jun 5, 2022

@author: AsifMahmud
'''
def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
    result = 0
    series_len = len(timeSeries)
    for i in range(series_len):
        if(i < series_len-1 and timeSeries[i] + duration > timeSeries[i+1]):
            result += timeSeries[i+1] - timeSeries[i]
        else:
            result += duration
    return result