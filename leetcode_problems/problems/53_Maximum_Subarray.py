'''
Created on Dec 3, 2021

@author: AsifMahmud
'''
def maxSubArray(self, nums) -> int:
    sum = 0
    maxSum = -9999999999
    for num in nums:
        sum += num
        if maxSum < sum:
            maxSum = sum
        if sum < 0:
            sum = 0
    return maxSum