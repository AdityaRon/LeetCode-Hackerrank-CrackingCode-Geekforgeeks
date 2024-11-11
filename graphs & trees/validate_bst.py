""" Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left 
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees. """


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid(node, minn, maxx):
            if not node:
                return True
            
            if node.val <= minn or node.val >= maxx:
                return False
            
            return is_valid(node.left, minn, node.val) and is_valid(node.right, node.val, maxx)
        
        return is_valid(root, float('-inf'), float('inf'))

        
