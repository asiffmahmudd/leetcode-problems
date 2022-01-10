'''
Created on Jan 9, 2022

@author: AsifMahmud
'''

def isHappy(self, n: int) -> bool:
    count = 0
    f = 0
    temp = n
    repeat = True
    arr = []
    while repeat == True:
        sum = 0
        arr.append(temp)
        while temp != 0 and repeat != False:
            sum += pow(temp%10, 2)
            temp = int(temp/10)
        if sum == 1:
            repeat = False
            f = 1
        elif sum in arr:
            repeat = False
        else:
            temp = sum
        
    if f == 1:
        return True
    else:
        return False