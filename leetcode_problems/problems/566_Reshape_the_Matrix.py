'''
Created on Jun. 19, 2022

@author: AsifMahmud
'''
def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    nums = []
    for row in range(len(mat)):
        for col in range(len(mat[row])):
            nums.append(mat[row][col])
    
    if(r*c != len(nums)):
        return mat
    
    index = 0
    result = []
    for row in range(r):
        temp = []
        for col in range(c):
            temp.append(nums[index])
            index += 1
        result.append(temp)
    return result