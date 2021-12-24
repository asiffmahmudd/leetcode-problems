'''
Created on Dec 23, 2021

@author: AsifMahmud
'''

def generate(self, numRows: int) -> List[List[int]]:
    i = 0
    result = []
    while(i < numRows):
        if i == 0:
            result.append([1])
        else:
            j = 0
            temp = []
            while(j <= i):
                if j == 0 or j == i:
                    temp.append(1)
                else:
                    temp.append(result[i-1][j-1]+result[i-1][j])
                j += 1
            result.append(temp)
        i += 1
    return result