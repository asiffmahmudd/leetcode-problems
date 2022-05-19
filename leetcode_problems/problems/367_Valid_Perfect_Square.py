'''
Created on May 19, 2022

@author: AsifMahmud
'''
def isPerfectSquare(self, num: int) -> bool:
    mid = num // 2
    start = 1
    end = num
    while start <= end:
        if mid*mid == num:
            return True
        elif mid*mid < num:
            start = mid+1
        else:
            end = mid-1
        mid = (start+end)//2
    return False