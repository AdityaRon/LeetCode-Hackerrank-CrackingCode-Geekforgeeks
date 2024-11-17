""" 
Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = []
        def dfs(root, isLeft):
            if root is None:
                return 
            if isLeft and root.left is None and root.right is None:
                ans.append(root.val)
                return
            dfs(root.left, True) 
            dfs(root.right, False)
        dfs(root, False)                 
        return sum(ans)

        
