'''
Created on May 22, 2022

@author: AsifMahmud
'''
def toHex(self, num: int) -> str:
    result = ""
    if num == 0:
        return "0"
    elif num < 0:
        num += 2**32
        
    while num:
        digit = num%16
        if digit > 9:
            result += chr(97+digit%10)
        else:
            result += str(digit)
        num = num // 16
    return result[::-1]