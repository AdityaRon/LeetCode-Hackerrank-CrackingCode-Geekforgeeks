class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # from collections import Counter
        # s_dict = Counter(s)
        # t_dict = Counter(t)
        # for word, freq in s_dict.items():
        #     if word in t_dict.keys() and t_dict[word] == freq:
        #         continue
        #     else:
        #         return False
        # return True
        # temp = ''
        # for index, word in enumerate(t):
        #     if word in s:
        #         temp += word
        # return temp == s
        i = 0
        j = 0
        while i <= len(s)-1 and j <= len(t)-1:
            if s[i] == t[j]:
                i +=1
            j +=1
        return i == len(s)
