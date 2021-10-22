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

#approach2

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        chars = {}
        maximum = 0
        if len(s) == len(set(s)):
            return -1
        else:
            for i,j in enumerate(s):
                if j not in chars:
                    chars[j] = [i]
                else:
                    chars[j].append(i)
            for key, value in chars.items():
                if (max(value)-min(value)-1) > maximum:
                    maximum = max(value)-min(value)-1
            return maximum
                    
