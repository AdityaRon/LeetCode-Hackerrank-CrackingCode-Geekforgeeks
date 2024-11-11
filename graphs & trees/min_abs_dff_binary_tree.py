""" Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

Input: root = [4,2,6,1,3]
Output: 1

"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        minDiff = [float('inf')]
        currentDiff = [None]

        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            
            if currentDiff[0] is not None:
                minDiff[0] = min(minDiff[0], node.val-currentDiff[0])
            currentDiff[0] = node.val

            dfs(node.right)
        dfs(root)
        return minDiff[0]        
        
