'''
Created on May 18, 2022

@author: AsifMahmud
'''
def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    num1_dict = {}
    num2_dict = {}
    
    for num in nums1:
        if(num in num1_dict.keys()):
            num1_dict[num] += 1
        else:
            num1_dict[num] = 1
    
    for num in nums2:
        if(num in num2_dict.keys()):
            num2_dict[num] += 1
        else:
            num2_dict[num] = 1
    
    result = []
    for key,val in num1_dict.items():
        if(key in num2_dict.keys()):
            n = min(val, num2_dict[key])
            for i in range(n):
                result.append(key)
    
    return result