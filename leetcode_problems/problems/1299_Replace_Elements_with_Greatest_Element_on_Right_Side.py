'''
Created on May 12, 2022

@author: AsifMahmud
'''
def replaceElements(self, arr: List[int]) -> List[int]:
    arr_len = len(arr)
    
    max_num = -1
    for i in range(arr_len-1, -1, -1):
        temp = arr[i]
        arr[i] = max_num
        max_num = max(temp, max_num)
    
    return arr