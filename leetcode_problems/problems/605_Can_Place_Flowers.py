'''
Created on Jun. 28, 2022

@author: AsifMahmud
'''

def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    list_len = len(flowerbed)
    if flowerbed[0] == 0:
        if list_len == 1:
            return True
        if flowerbed[1] == 0:
            n -= 1
            flowerbed[0] = 1
    for i in range(1, list_len-1):
        if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
            flowerbed[i] = 1
            n -= 1
        if n <= 0:
            break
            
    if flowerbed[list_len-1] == 0:
        if list_len - 2 >= 0 and flowerbed[list_len-2] == 0:
            n -= 1
            flowerbed[list_len - 1] = 1
    return True if n <= 0 else False