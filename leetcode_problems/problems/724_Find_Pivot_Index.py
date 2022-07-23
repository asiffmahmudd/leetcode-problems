'''
Created on Jul. 23, 2022

@author: AsifMahmud
'''
def pivotIndex(self, nums: List[int]) -> int:
    leftSum, rightSum, numsLen = 0, sum(nums), len(nums)
    
    for i in range(numsLen):
        rightSum -= nums[i]
        if(leftSum == rightSum):
            return i
        leftSum += nums[i]
    return -1