""" Given a binary tree, determine if it is 
height-balanced.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
 """

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = [True]
        def height(root):
            if root is None:
                return 0
            left = height(root.left)
            right = height(root.right)

            if abs(left - right) > 1:
                balanced[0] = False
                return 0
            
            return 1 + max(left, right)
        height(root)
        return balanced[0]
        
