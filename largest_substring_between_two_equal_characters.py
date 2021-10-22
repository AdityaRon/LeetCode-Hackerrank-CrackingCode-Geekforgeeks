class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        if len(s) == len(set(s)):
            return -1
        elif len(set(s)) == 1:
            return 0
        else:
            maxcount = 0
            for i,j in enumerate(s):
                count = 0
                for k in s[i+1:]:
                    if j == k:
                        maxcount = max(count, maxcount)
                        count+=1
                    else:
                        count +=1
            return maxcount
