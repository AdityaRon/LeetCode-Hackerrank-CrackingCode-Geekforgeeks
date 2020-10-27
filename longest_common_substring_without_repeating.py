class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        self.s = s
        seenStrings = {}
        result = 0
        start = 0
        for i,j in enumerate(s):
            if j not in seenStrings or seenStrings.get(j,0) < start:
                result = max(result, (i-start) +1)
            else:
                start = seenStrings[j] + 1
            seenStrings[j] = i
        print(seenStrings)
        return result
