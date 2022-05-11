'''
Created on May 10, 2022

@author: AsifMahmud
'''
def sortedSquares(self, nums: List[int]) -> List[int]:
    result = []
    isFirst = True
    
    result = [num**2 for num in nums] 
    result.sort()
        
    return result