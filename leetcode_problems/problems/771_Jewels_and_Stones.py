'''
Created on Aug. 12, 2022

@author: AsifMahmud
'''
def numJewelsInStones(self, jewels: str, stones: str) -> int:
    count = 0
    for stone in stones:
        if stone in jewels:
            count += 1
    return count