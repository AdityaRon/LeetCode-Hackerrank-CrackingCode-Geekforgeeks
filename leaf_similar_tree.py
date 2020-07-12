class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        self.root1 = root1
        self.root2 = root2
        def leaves(root):
            if not root:
                return []
            if not (root.left or root.right):
                return [root.val]
            return leaves(root.left) + leaves(root.right)
        return leaves(root1) == leaves(root2)
