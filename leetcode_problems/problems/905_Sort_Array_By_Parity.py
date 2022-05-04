'''
Created on May 3, 2022

@author: AsifMahmud
'''
def sortArrayByParity(self, nums: List[int]) -> List[int]:
    result = []
    for num in nums:
        if(num % 2 == 0):
            result.append(num)
    for num in nums:
        if(num % 2 != 0):
            result.append(num)
    return result