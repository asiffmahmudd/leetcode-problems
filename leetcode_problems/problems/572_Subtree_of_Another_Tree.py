'''
Created on Sep. 5, 2022

@author: AsifMahmud
'''
def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    if not subRoot:
        return True
    if not root:
        return False
    if self.isSameTree(root, subRoot):
        return True
    return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

def isSameTree(self, tree1, tree2):
    if not tree1 and not tree2:
        return True
    if tree1 and tree2 and tree1.val == tree2.val:
        return (self.isSameTree(tree1.left, tree2.left) and self.isSameTree(tree1.right, tree2.right))
    return False
    