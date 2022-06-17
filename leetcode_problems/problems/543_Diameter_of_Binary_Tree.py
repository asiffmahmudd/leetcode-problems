'''
Created on Jun. 17, 2022

@author: AsifMahmud
'''
def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    def maxDepth(root):
        if not root:
            return 0
        leftDepth = maxDepth(root.left)
        rightDepth = maxDepth(root.right)
        totalDiameter = leftDepth + rightDepth
        self.maxDiameter = max(self.maxDiameter, totalDiameter)
        
        return max(leftDepth, rightDepth) + 1
        
    self.maxDiameter = 0
    maxDepth(root)
    return self.maxDiameter