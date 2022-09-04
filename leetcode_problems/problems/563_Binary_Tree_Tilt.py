'''
Created on Sep. 4, 2022

@author: AsifMahmud
'''
def findTilt(self, root: Optional[TreeNode]) -> int:
        
    def findTilt(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def getTilt(root):
            nonlocal ans
            if not root:
                return 0
            leftSub = getTilt(root.left)
            rightSub = getTilt(root.right)
            ans += abs(leftSub - rightSub)
            return root.val + leftSub + rightSub 
        getTilt(root)
        return ans