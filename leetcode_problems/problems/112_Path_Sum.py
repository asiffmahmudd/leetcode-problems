'''
Created on Feb 13, 2022

@author: AsifMahmud
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        def traverseTree(root, targetSum):
            if root:
                targetSum -= root.val
                if root.left == None and root.right == None and targetSum == 0:
                    return True
                else:
                    return traverseTree(root.left, targetSum) or traverseTree(root.right, targetSum) 
            
        
        return traverseTree(root, targetSum)
        