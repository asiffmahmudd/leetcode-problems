'''
Created on May 25, 2022

@author: AsifMahmud
'''
def addStrings(self, num1: str, num2: str) -> str:
    num1_len = len(num1)
    num2_len = len(num2)
    if num1_len < num2_len:
        num1 = (num2_len-num1_len)*"0" + num1
    elif num2_len < num1_len:
        num2 = (num1_len-num2_len)*"0" + num2
    
    carry = 0
    result = ""
    digitsSum = ""
    for digit1, digit2 in zip(num1[::-1], num2[::-1]):
        if carry == 0:
            digitsSum = (ord(digit1) + ord(digit2)) % ord('0')
        else:
            digitsSum = (ord(digit1) + ord(digit2) + 1) % ord('0')
            carry = 0
        if(digitsSum >= 10):
            carry = 1
            result = chr(ord('0') + digitsSum%10) + result
        else:
            result = chr(ord('0') + digitsSum) + result
            
    if carry == 1:
        result = "1" + result
    return result