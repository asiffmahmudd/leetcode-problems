'''
Created on Jul. 1, 2022

@author: AsifMahmud
'''
def findMaxAverage(self, nums: List[int], k: int) -> float:
    index = 0
    sum, maxAvg = 0, -99999
    for i in range(len(nums)):
        sum += nums[i]
        if i >= k-1:
            avg = sum/k
            if maxAvg < avg:
                maxAvg = avg
            sum -= nums[index]
            index += 1
    return maxAvg