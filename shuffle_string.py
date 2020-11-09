class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        self.s = s
        self.indices = indices
        changedString = list(s)
        j = 0
        for i in indices:
            changedString[i] = s[j]
            j+=1
        return ''.join(changedString)
