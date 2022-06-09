'''
Created on Jun 9, 2022

@author: AsifMahmud
'''
def convertToBase7(self, num: int) -> str:
    if num == 0:
        return "0"

    result = ""
    temp = abs(num)
    
    while(temp):
        result += str(temp%7)
        temp = int(temp/7)
    result = result[::-1]
    
    if num < 0:
        result = "-" + result
    return result