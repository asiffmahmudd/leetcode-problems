'''
Created on Jan 5, 2022

@author: AsifMahmud
'''

def majorityElement(self, nums: List[int]) -> int:
    elm_count = 0
    elm = 0
    elements = {}
    for elm in nums:
        if elm in elements:
            elements[elm] += 1
        else:
            elements[elm] = 1
    
    majority = 0
    for key in elements:
        if(elements[key] > majority):
            majority = elements[key]
            majority_element = key
    return majority_element