""" Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

Example 1:

Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true


Constraints:

The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(left, right):
            if not left and not right:
                return True
            if (not left and right) or (not right and left):
                return False
            if left.val != right.val:
                return False
            return isSameTree(left.left, right.left) and isSameTree(left.right, right.right)
        
        def has_subtree(root):
            if not root:
                return False
            
            if isSameTree(root, subRoot):
                return True
            
            return has_subtree(root.left) or has_subtree(root.right)

        return has_subtree(root)
        
        
