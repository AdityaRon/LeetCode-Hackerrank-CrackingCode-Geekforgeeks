class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        j = 0
        substring = 0
        match = False
        if len(s) == 1 and len(t) == 1 and s != t:
            return 1
        if len(t) == 0:
            return 0
        while i <= len(t) - 1 and j <= len(s) - 1:
            if t[i] == s[j]:
                match = True
                substring = i
                i += 1
            j += 1
        #print(substring, match, t[substring+1:], len(t[substring+1:]))
        if match:
            return len(t[substring+1:])
        else:
            return len(t)

            


        
