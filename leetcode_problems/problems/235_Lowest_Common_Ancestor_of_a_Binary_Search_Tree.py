'''
Created on Feb 21, 2022

@author: AsifMahmud
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val > p.val and root.val > q.val:
            self.lowestCommonAncestor(root.left, p, q)
        if root.val < p.val and root.val < q.val:
            self.lowestCommonAncestor(root.right, p, q)
        return root
            
            