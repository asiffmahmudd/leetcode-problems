def countNodes(self, root: Optional[TreeNode]) -> int:
    if root:
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    else:
        return 0