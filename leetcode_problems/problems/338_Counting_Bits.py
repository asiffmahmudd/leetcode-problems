'''
Created on Mar 4, 2022

@author: AsifMahmud
'''
def countBits(self, n: int) -> List[int]:
    result = []
    for i in range(n+1):
        numBin = bin(i).replace("0b", "")
        ones = [1 for digit in numBin if digit == "1"]
        result.append(len(ones))
    return result