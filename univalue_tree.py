# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        self.root = TreeNode
        result = []
        def preorder(root, result):
            if root != None:
                result.append(root.val)
                preorder(root.left,result)
                preorder(root.right,result)
        preorder(root, result)
        return sum(result)/len(result) == root.val
