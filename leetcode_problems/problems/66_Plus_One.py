'''
Created on Dec 4, 2021

@author: AsifMahmud
'''
def plusOne(self, digits: List[int]) -> List[int]:
    result = []
    count = 0
    shouldCount = True
    for num in reversed(digits):
        if shouldCount == True and num == 9:
            result = [0] + result
            count = 1
        elif (shouldCount == True and num != 9) or (num != 9 and count == 1):
            shouldCount = False
            count = 0
            result = [num+1] + result
        else:
            result = [num] + result
            shouldCount = False
            count = 0
    if(shouldCount == True and count == 1):
        result = [1] + result
    return result