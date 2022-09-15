'''
Created on Sep. 14, 2022

@author: AsifMahmud
'''
def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
    arr = sorted(set(self.treeToList(root)))
    if len(arr) < 2:
        return -1
    else:
        return arr[1]
    
def treeToList(self, root):
    if root is None:
        return []
    return self.treeToList(root.left) + [root.val] + self.treeToList(root.right)
