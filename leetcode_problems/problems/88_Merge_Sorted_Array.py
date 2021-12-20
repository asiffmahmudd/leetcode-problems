'''
Created on Dec 20, 2021

@author: AsifMahmud
'''
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    i = 0
    len1 = len(nums1)
    len2 = len(nums2)
    for x in range(len1-len2, len1):
        nums1[x] = nums2[i]
        i += 1
    nums1.sort()
        