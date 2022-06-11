'''
Created on Jun 10, 2022

@author: AsifMahmud
'''
def checkPerfectNumber(self, num: int) -> bool:
    if num == 1:
        return False
    divisorsSum = 1
    start = 2
    
    while(start**2 <= num):
        if num % start == 0:
            divisorsSum += start + (num//start)
        start += 1
    
    return num == divisorsSum