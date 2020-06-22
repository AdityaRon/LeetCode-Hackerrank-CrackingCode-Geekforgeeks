# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.root = root
        def height(root):
            if root is None:
                return 0
            rightHeight = height(root.right)
            leftHeight = height(root.left)
            return 1 + max(rightHeight,leftHeight)
        return height(root)
