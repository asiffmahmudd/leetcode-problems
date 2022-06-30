'''
Created on Jun. 29, 2022

@author: AsifMahmud
'''
def maximumProduct(self, nums: List[int]) -> int:
    numsLen = len(nums)
    nums.sort()
    return max(nums[0]*nums[1]*nums[numsLen-1], nums[numsLen-1]*nums[numsLen-2]*nums[numsLen-3])