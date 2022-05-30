'''
Created on May 30, 2022

@author: AsifMahmud
'''
def islandPerimeter(self, grid: List[List[int]]) -> int:
    rows = len(grid)
    perimeter = 0
    
    for i in range(rows):
        cols = len(grid[i])
        for j in range(cols):
            if(grid[i][j]):
                if(i == 0 or (i > 0 and grid[i-1][j] == 0)):
                    perimeter += 1
                if(j == cols-1 or (j < cols-1 and grid[i][j+1] == 0)):
                    perimeter += 1
                if(i == rows-1 or (i < rows-1 and grid[i+1][j] == 0)):
                    perimeter += 1
                if(j == 0 or (j > 0 and grid[i][j-1] == 0)):
                    perimeter += 1
    return perimeter