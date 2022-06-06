'''
Created on Jun 6, 2022

@author: AsifMahmud
'''
def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    ans = []
    nums2_len = len(nums2)
    for num1 in nums1:
        greater = -1
        index = nums2.index(num1)
        for i in range(index+1, nums2_len):
            if(nums2[i] > num1):
                greater = nums2[i]
                break
        ans.append(greater)
        
    return ans