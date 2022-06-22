'''
Created on Jun. 22, 2022

@author: AsifMahmud
'''
def findLHS(self, nums: List[int]) -> int:
    frequency = dict(Counter(nums))
    maxCount = 0
    
    for key in frequency:
        if key+1 in frequency:
            maxCount = max(frequency[key] + frequency[key+1], maxCount)
    return maxCount
            