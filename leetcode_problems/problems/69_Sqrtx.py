'''
Created on Dec 17, 2021

@author: AsifMahmud
'''
def mySqrt(self, x: int) -> int:
    if x == 0 or x == 1:
        return x
    else:
        i = 2
        while(i*i < x):
            i = i+1
        if i*i == x:
            return i
        else:
            return i-1