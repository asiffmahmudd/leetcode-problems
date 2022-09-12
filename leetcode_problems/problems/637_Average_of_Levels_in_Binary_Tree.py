'''
Created on Sep. 12, 2022

@author: AsifMahmud
'''
def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
    ans = []
    queue = collections.deque([root])
    
    while(queue):
        size = len(queue)
        sum = 0
        for _ in range(size):
            treeNode = queue.popleft() 
            sum += treeNode.val
            if treeNode.left:
                queue.append(treeNode.left)
            if treeNode.right:
                queue.append(treeNode.right)
        ans.append(sum/size)
        
    return ans