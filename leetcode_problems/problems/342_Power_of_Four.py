'''
Created on Mar 6, 2022

@author: AsifMahmud
'''
def isPowerOfFour(self, n: int) -> bool:
    if n < 0:
        return False
    for i in range(19):
        if(math.pow(4, i) == n):
            return True
    return False