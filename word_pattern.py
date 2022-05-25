class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        self.pattern = pattern
        self.s = s  
        result = {}
        pattern = list(pattern)
        s = s.split(' ')
        if len(s) != len(pattern):
            return False
        if len(s) == 1 and len(pattern) == 1:
            return True
        for i,j in zip(pattern,s):
            if i not in result:
                result[i] = j
            elif result[i] == j:
                continue
            else:
                return False
        return False if len(set(result.keys())) != len(set(result.values())) else True
                                         
