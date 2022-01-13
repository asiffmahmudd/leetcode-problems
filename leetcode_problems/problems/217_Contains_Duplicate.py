'''
Created on Jan 13, 2022

@author: AsifMahmud
'''

def containsDuplicate(self, nums: List[int]) -> bool:
    list_len = len(nums)
    if list_len == 1:
        return False
    nums.sort()
    list_len -= 1
    for i in range(list_len):
        if nums[i] == nums[i+1]:
            return True
    return False