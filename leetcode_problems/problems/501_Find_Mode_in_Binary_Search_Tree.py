'''
Created on Jun 6, 2022

@author: AsifMahmud
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(root, arr):
            if root:
                arr.append(root.val)
                traverse(root.left, arr)
                traverse(root.right, arr)
            
        arr = []
        traverse(root, arr)
        frequency = dict(Counter(arr))
        result = []
        max_val = max(frequency.values())
        
        for key, value in frequency.items():
            if value == max_val:
                result.append(key)
        return result