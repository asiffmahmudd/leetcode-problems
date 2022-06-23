'''
Created on Jun. 23, 2022

@author: AsifMahmud
'''
def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
    minRow = m
    minCol = n
    for i in range(len(ops)):
        if ops[i][0] < minRow:
            minRow = ops[i][0]
        if ops[i][1] < minCol:
            minCol = ops[i][1]
            
    return minRow*minCol