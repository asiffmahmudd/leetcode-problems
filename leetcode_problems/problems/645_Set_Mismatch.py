'''
Created on Jul. 2, 2022

@author: AsifMahmud
'''
def findErrorNums(self, nums: List[int]) -> List[int]:
    n = len(nums)
    numsDict = dict(Counter(nums))
    result = {}
    for i in range(1, n+1):
        if i not in numsDict.keys():
            result["second"] = i
        elif numsDict[i] > 1:
            result["first"] = i
    return [result["first"], result["second"]]