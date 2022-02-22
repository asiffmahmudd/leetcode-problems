'''
Created on Feb 22, 2022

@author: AsifMahmud
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def traverseTree(root, result, currStr):
            if(root):
                if(not root.left and not root.right):
                    currStr += str(root.val)
                    result.append(currStr)
                else:
                    currStr += str(root.val)+"->"
                traverseTree(root.left, result, currStr)
                traverseTree(root.right, result, currStr)
        result = []
        traverseTree(root, result, "")
        return result