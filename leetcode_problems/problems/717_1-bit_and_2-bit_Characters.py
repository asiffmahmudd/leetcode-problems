'''
Created on Jul. 21, 2022

@author: AsifMahmud
'''
def isOneBitCharacter(self, bits: List[int]) -> bool:
    index = 0
    lastIndex = len(bits) - 1
    while(index < lastIndex):
        if bits[index] == 1:
            index += 2
        else:
            index += 1
    return index == lastIndex 