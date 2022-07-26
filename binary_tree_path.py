class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.root = root
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        totalPath = [str(root.val)+"->"+left for left in self.binaryTreePaths(root.left)]
        totalPath += [str(root.val)+"->"+right for right in self.binaryTreePaths(root.right)]
        return totalPath
