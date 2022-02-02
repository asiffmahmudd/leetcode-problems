'''
Created on Feb 2, 2022

@author: AsifMahmud
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if(root == None):
            return False
        def checkSymmetric(root1, root2):
            if(root1 == None and root2 == None):
                return True
            elif(root1 == None or root2 == None or root1.val != root2.val):
                return False
            else:
                return checkSymmetric(root1.left, root2.right) and checkSymmetric(root1.right, root2.left)
        
        return checkSymmetric(root, root)
        