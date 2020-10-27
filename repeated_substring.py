class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        self.s = s
        #print(s[1:] + s[:-1])
        return s in (s[1:] + s[:-1])
