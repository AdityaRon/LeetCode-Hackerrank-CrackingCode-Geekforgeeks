# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Given the root of a binary tree, return its depth.

# The depth of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.

# Input: root = [1,2,3,null,null,4]

# Output: 3

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def compute_height(root, current):
            if root is None:
                return current

            return max(compute_height(root.left, current+1), compute_height(root.right, current+1))

        return compute_height(root, 0)
