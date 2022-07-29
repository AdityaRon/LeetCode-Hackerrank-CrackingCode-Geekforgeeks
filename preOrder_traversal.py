# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.root = root
        results = []
        if not root:
            return []
#         if root:
#             results += [root.val]
#         results += self.preorderTraversal(root.left)
#         results += self.preorderTraversal(root.right)
#         return results
        stack = []
        stack.append(root)
        while (len(stack) > 0):
            temp = stack.pop()
            results.append(temp.val)
            if temp.right:
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)
        return results
        
        
