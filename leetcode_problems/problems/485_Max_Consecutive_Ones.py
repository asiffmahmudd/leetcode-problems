'''
Created on May 31, 2022

@author: AsifMahmud
'''
def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    max = 0
    count = 0
    for num in nums:
        if num == 0:
            if max < count:
                max = count
            count = 0
        else:
            count += 1
    if max < count:
        max = count
    return max