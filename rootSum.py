def rootSum(root, target, results):
    if root is None:
        return False
    if root.left is None and root.right is None:
        if root.val == target:
            results.append(root.val)
            return True
        else:
            return False
    if rootSum(root.left, target-root.val, results) or rootSum(root.right, target-root.val, results):
        results.append(root.val)
        return True
    return False
