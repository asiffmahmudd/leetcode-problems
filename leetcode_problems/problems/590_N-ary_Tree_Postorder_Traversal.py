'''
Created on Sep. 23, 2022

@author: AsifMahmud
'''
def postorder(self, root: 'Node') -> List[int]:
    if root is None:
        return []
    result = []
    if root.children:
        for node in root.children:
            result.extend(self.postorder(node))
    result.append(root.val)
    return result