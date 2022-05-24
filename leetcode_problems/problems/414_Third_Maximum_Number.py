'''
Created on May 23, 2022

@author: AsifMahmud
'''
def thirdMax(self, nums: List[int]) -> int:
    nums = list(set(nums))
    nums.sort(reverse=True)
    if len(nums) >= 3:
        return nums[2]
    else:
        return max(nums)