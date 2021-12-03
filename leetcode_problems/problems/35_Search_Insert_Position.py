'''
Created on Nov 28, 2021

@author: AsifMahmud
'''

def searchInsert(self, nums, target):
        low = 0
        high = len(nums)
        mid = int((high+low)/2)
        result = None
        while(low < high):
            if nums[mid] == target:
                result = mid
                break
            elif target > nums[mid]:
                low = mid+1
            else:
                high = mid
            mid = int((high+low)/2)
        if(result == None):
            result = low
        
        return result