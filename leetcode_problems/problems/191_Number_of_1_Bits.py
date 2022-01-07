'''
Created on Jan 7, 2022

@author: AsifMahmud
'''
def hammingWeight(self, n: int) -> int:
    binary = format(n,"b")
    count = 0
    for bit in binary:
        if bit == '1':
            count += 1
    return count        
    