class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.s = s
        s1 = {}
        output = []
        def unique(s):
            from collections import Counter
            s1 = Counter(s)
            for i,j in s1.items():
                if j == 1:
                    output.append(s.index(i))
            if output != []:
                return min(output)
            else:
                return (-1)
        if s == "" or s == set(s):
            return (-1)
        else:
            return (unique(s))
            
