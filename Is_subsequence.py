class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
#         substringlist = list(s)
#         originallist = list(t)
#         for i in t:
#             if i not in substringlist:
#                 originallist.remove(i)
#         return (''.join(originallist) == ''.join(substringlist))

        startT = 0
        startS = 0
        while startT < len(t) and startS < len(s):
            if t[startT] == s[startS]:
                startS+=1
            startT+=1
        return startS == len(s)
