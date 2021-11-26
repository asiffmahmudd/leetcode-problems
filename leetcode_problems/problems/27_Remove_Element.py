'''
Created on Nov 26, 2021

@author: AsifMahmud
'''
def removeElement(self, nums, val) -> int:
        count = 0
        for x in nums:
            if x != val:
                nums[count] = x 
                count += 1
        return count