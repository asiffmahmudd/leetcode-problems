'''
Created on Jan 25, 2022

@author: AsifMahmud
'''
def climbStairs(self, n: int) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        prev = 1
        current = 2
        sum = 0
        for i in range(3, n+1):
            temp = current
            current = prev+current
            prev = temp
        return current