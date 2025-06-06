""" Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children. """

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        currentSum = 0
        def isPathsum(node, currentSum):
            if not node:
                return False
            currentSum += node.val
            if not node.left and not node.right:
                print(currentSum)
                if currentSum == targetSum:
                    return True
                else:
                    return False
            return isPathsum(node.left, currentSum) or isPathsum(node.right, currentSum)

        return isPathsum(root, currentSum)


            

            
        
