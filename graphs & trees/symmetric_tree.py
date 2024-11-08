""" Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center). 

Input: root = [1,2,2,3,4,4,3]
Output: true

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSame(left, right):
            if left is None and right is None:
                return True
            if (left is None and right is not None) or (left is not None and right is None):
                return False
            if left.val != right.val:
                return False    
            return isSame(left.left, right.right) and isSame(left.right, right.left)
        return isSame(root.left, root.right)
