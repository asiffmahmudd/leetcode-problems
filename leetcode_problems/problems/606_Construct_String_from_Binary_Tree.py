'''
Created on Sep. 5, 2022

@author: AsifMahmud
'''
def tree2str(self, root: Optional[TreeNode]) -> str:
    if root is None:
        return ''
    if not root.left and not root.right:
        return str(root.val)
    leftStr = self.tree2str(root.left)
    rightStr = self.tree2str(root.right)
    if rightStr and not leftStr:
        return str(root.val) + '()' + '(' + rightStr + ')'
    if leftStr and not rightStr:
        return str(root.val) + '(' + leftStr + ')'
    
    return str(root.val) + '(' + leftStr + ')(' + rightStr + ')'