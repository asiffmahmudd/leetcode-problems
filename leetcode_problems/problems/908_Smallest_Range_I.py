'''
Created on May 5, 2022

@author: AsifMahmud
'''
def smallestRangeI(self, nums: List[int], k: int) -> int:
    max_num = max(nums) - k 
    min_num = min(nums) + k
    num_range
    if(min_num >= max_num):
        return 0
    else:
        return max_num - min_num