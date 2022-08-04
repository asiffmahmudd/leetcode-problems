'''
Created on Aug. 3, 2022

@author: AsifMahmud
'''
def dominantIndex(self, nums: List[int]) -> int:
    temp = sorted(nums, reverse=True)
    return nums.index(temp[0]) if temp[0] >= temp[1]*2 else -1