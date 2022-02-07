'''
Created on Feb 6, 2022

@author: AsifMahmud
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        return  self.makeBST(nums, 0, len(nums)-1)
    
    def makeBST(self, nums, start, end):
        if(start > end):
            return None
        mid = (int)((start+end)/2)
        
        root = TreeNode(nums[mid], None, None)
        root.left = self.makeBST(nums, start, mid-1)
        root.right = self.makeBST(nums, mid+1, end)
        return root