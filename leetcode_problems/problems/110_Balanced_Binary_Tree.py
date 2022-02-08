'''
Created on Feb 7, 2022

@author: AsifMahmud
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        leftTree = self.calculateDepth(root.left)
        rightTree = self.calculateDepth(root.right)
        if abs(leftTree-rightTree) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        else:
            return False
        
    def calculateDepth(self, root):
        if root:
            return 1 + max(self.calculateDepth(root.left), self.calculateDepth(root.right))
        else:
            return 0