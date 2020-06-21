class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        import sys
        self.root = root
        minimum = -sys.maxsize-1
        maximum = sys.maxsize+1
        def isBst(root,minimum, maximum):
            if root == None:
                return True
            elif root.val <= minimum or root.val >= maximum:
                return False
            else:
                return isBst(root.left, minimum, root.val) and isBst(root.right, root.val, maximum)
        return isBst(root, minimum, maximum)
                
