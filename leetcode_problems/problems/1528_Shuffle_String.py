'''
Created on May 1, 2022

@author: AsifMahmud
'''
def restoreString(self, s: str, indices: List[int]) -> str:
        len_arr = len(indices)
        result = [None] * len_arr
        
        for index in range(len_arr):
            result[indices[index]] = s[index] 
            
        return "".join(result)