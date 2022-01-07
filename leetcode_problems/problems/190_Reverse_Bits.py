'''
Created on Jan 6, 2022

@author: AsifMahmud
'''
def reverseBits(self, n: int) -> int:
    binary = '{:032b}'.format(n, "b")
    reverse_binary = binary[::-1]
    return int(reverse_binary, 2)