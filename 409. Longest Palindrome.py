class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_dict = {}
        res = 0
        val = 0
        if len(s) == 1:
            return 1
        for char in s:
            char_dict[char] = char_dict.get(char, 0) + 1
        for key, value in char_dict.items():
            if value % 2 == 0:
                res += value
            else:
                res += value - 1
                val = 1
        return res + val


        
