'''
Created on May 21, 2022

@author: AsifMahmud
'''
def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
    def traverseTree(node, isLeft):
        if node:
            traverseTree(node.left, True)
            if isLeft and node.left == None and node.right == None:
                self.sumOfLeft += node.val
            traverseTree(node.right, False)
    
    self.sumOfLeft = 0  
    traverseTree(root, False)
    return self.sumOfLeft