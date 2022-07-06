'''
Created on Jul. 5, 2022

@author: AsifMahmud
'''
def findLengthOfLCIS(self, nums: List[int]) -> int:
    count = 1
    numsLen = len(nums)
    temp = 1
    for i in range(1, numsLen):
        if nums[i] > nums[i-1]:
            temp += 1
        else:
            if temp > count:
                count = temp
            temp = 1
    if temp > count:
        count = temp
    return count