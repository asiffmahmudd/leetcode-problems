'''
Created on Jul. 21, 2022

@author: AsifMahmud
'''
def findShortestSubArray(self, nums: List[int]) -> int:
    frequency = dict(Counter(nums))
    degree = max(frequency.values())
    numsLen = len(nums)
    result = numsLen
    for key in frequency:
        if(frequency[key] == degree):
            start = nums.index(key)
            end = numsLen - nums[::-1].index(key)
            if(len(nums[start:end]) < result):
                result = len(nums[start:end])
    return result