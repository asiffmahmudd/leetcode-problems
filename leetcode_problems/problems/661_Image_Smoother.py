'''
Created on Jul. 11, 2022

@author: AsifMahmud
'''
def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
    m = len(img)
    result = [[0]*m for i in range(m)]
    for i in range(m):
        n = len(img[i])
        for j in range(n):
            count = 1
            sum = img[i][j]
            if i-1 >= 0:            
                sum += img[i-1][j]
                count += 1
            if j-1 >= 0:            
                sum += img[i][j-1]
                count += 1
            if i-1 >= 0 and j-1 >= 0: 
                sum += img[i-1][j-1]
                count += 1
            if i+1 < m:            
                sum += img[i+1][j]
                count += 1
            if j+1 < n:           
                sum += img[i][j+1]
                count += 1
            if i+1 < m and j+1 < n:
                sum += img[i+1][j+1]
                count += 1
            if i-1 >= 0 and j+1 < n: 
                sum += img[i-1][j+1]
                count += 1
            if i+1 < m and j-1 >= 0: 
                sum += img[i+1][j-1]
                count += 1
            result[i][j] = floor(sum/count)
            
    return result