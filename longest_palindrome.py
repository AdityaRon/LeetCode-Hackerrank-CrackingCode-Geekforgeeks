class Solution:
    def longestPalindrome(self, s: str) -> int:
        self.s = s
        if len(set(s)) > 1:
            results = {}
            long = 0
            for i in s:
                results[i] = results.get(i,0) + 1
            #print(results)
            for i,j in results.items():
                if j % 2 == 0 and j > 1:
                    long +=j
                else:
                    long += j-1
            return long if len(s) == long else long + 1
        else:
            return len(s)
                
