'''
Created on Aug. 7, 2022

@author: AsifMahmud
'''
def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
    rows = len(matrix) 
    cols = len(matrix[0])
    
    for i in range(0, rows):
        col = 1
        num = matrix[i][0]
        for j in range(i+1, rows):
            if col >= cols:
                break
            if matrix[j][col] != num:
                return False
            col += 1
            
    for i in range(1, cols):
        row = 1
        num = matrix[0][i]
        for j in range(i+1, cols):
            if row >= rows:
                break
            if matrix[row][j] != num:
                return False
            row += 1
    return True