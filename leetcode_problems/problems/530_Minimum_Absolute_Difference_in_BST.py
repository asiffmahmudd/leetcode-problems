'''
Created on Jun. 15, 2022

@author: AsifMahmud
'''
def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
    def traverse(root, arr):
        if root:
            self.arr.append(root.val)
            traverse(root.left, self.arr)
            traverse(root.right, self.arr)
    
    self.arr = []
    traverse(root, self.arr)
    self.arr.sort()
    
    minDiff = 99999999
    for i in range(len(self.arr)-1):
        diff = abs(self.arr[i]-self.arr[i+1])
        if diff < minDiff:
            minDiff = diff
    return minDiff