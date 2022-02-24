'''
Created on Feb 24, 2022

@author: AsifMahmud
'''
def addDigits(self, num: int) -> int:
    while len(str(num)) != 1:
        temp = [int(digit) for digit in str(num)]
        num = sum(temp)
    return num