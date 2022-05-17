'''
Created on May 16, 2022

@author: AsifMahmud
'''
def __init__(self, nums: List[int]):
    self.sumList = []
    for n in nums:
        self.sumList.append((n + self.sumList[-1]) if self.sumList else n)

def sumRange(self, left: int, right: int) -> int:
    if not left:
        return self.sumList[right]
    else:
        return self.sumList[right] - self.sumList[left-1]
