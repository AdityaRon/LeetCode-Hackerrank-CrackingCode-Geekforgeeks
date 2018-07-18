class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        self.A = A
        def rev(B):
            revlist = []
            i = len(B)-1
            while i >= 0:
                revlist.append(B[i])
                i -= 1
            return (revlist)
        def invert(B):
            inv = []
            for i in B:
                if i == 0:
                    inv.append(1)
                else:
                    inv.append(0)  
            return(inv)
        output = []
        temp = []       
        for i in (A):
            temp = rev(i)
            output.append(invert(temp))
        return(output)
            
            
