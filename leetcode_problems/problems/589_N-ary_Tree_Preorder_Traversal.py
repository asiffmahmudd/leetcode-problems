'''
Created on Sep. 20, 2022

@author: AsifMahmud
'''
def preorder(self, root: 'Node') -> List[int]:
    result = []
    if root is None:
        return []
    result.append(root.val)
    if root.children:
        for child in root.children:
            result.extend(self.preorder(child))
    return result
        