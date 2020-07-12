def deepestLeavesSumroot(TreeNode):
    root = TreeNode
    q, lastlevel = [root], []
    while q:
        nextlevel = []
        n = len(q)
        for i in range(n):
            #print(i)
            node = q.pop()
            for child in node.left, node.right:
                if child:
                    nextlevel.append(child)
            print(nextlevel)
        q = nextlevel
        if nextlevel:
            lastlevel = nextlevel[:]
    return sum([node.val for node in lastlevel])
