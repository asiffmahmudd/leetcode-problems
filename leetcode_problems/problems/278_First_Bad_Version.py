'''
Created on May 13, 2022

@author: AsifMahmud
'''
def firstBadVersion(self, n: int) -> int:
    mid = n // 2
    left = 1
    right = n
    while(left <= right):
        check = isBadVersion(mid)
        if(check and not isBadVersion(mid-1)):
            return mid
        elif(check):
            right = mid - 1
        else:
            left = mid + 1
        mid = (right + left) // 2