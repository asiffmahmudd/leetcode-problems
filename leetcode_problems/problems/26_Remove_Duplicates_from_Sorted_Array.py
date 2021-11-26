'''
Created on Nov 25, 2021

@author: AsifMahmud
'''

def removeDuplicates(self, nums) -> int:
    list_len = len(nums)
    prev_index = 0
    
    loop_range = range(1, list_len)
    for i in loop_range:
        if nums[prev_index] != nums[i]:
            nums[prev_index+1] = nums[i]
            prev_index += 1
    
    return prev_index+1