'''
Created on Jul. 27, 2022

@author: AsifMahmud
'''
def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    def repeat(row, col, image, visited, color, prevColor):
        if(row < 0 or row >= len(image) or col < 0 or col >= len(image[0]) or visited[row][col] or image[row][col] != prevColor):
            return
        visited[row][col] = True
        image[row][col] = color
        repeat(row, col+1, image, visited, color, prevColor)
        repeat(row, col-1, image, visited, color, prevColor)
        repeat(row+1, col, image, visited, color, prevColor)
        repeat(row-1, col, image, visited, color, prevColor)
        
    visited = [[False]*len(image[0]) for i in range(len(image))]
    prevColor = image[sr][sc]
    repeat(sr, sc, image, visited, color, prevColor)
    return image