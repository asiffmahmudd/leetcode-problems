'''
Created on May 11, 2022

@author: AsifMahmud
'''
def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    nums = nums1 + nums2
    nums = sorted(nums)
    nums_len = len(nums)
    if nums_len % 2 == 1:
        return nums[int(nums_len/2)]
    else:
        return (nums[math.floor(nums_len/2)] + nums[math.floor(nums_len/2) - 1]) / 2