""" 230. Kth Smallest Element in a BST 

Input: root = [3,1,4,null,2], k = 1
Output: 1

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # elements = []
        # def bst_traversal(root):
        #     if not root:
        #         return 
        #     bst_traversal(root.left)
        #     elements.append(root.val)
        #     bst_traversal(root.right)
        # bst_traversal(root)
        # return elements[k-1]
      count = [k]
      ans = [0]
      def dfs(root):
            if not root:
                return 
            dfs(root.left)
            if count[0] == 1:
                ans[0] = root.val
            count[0] -= 1
            if count[0] > 0:
                dfs(root.right)
      dfs(root)
      return ans[0]
        
          
        
        
