class Solution:
    def longestPalindrome(self, s: str) -> str:
        def valid_palindrome(s,start,end):
            while start >= 0 and end < len(s) and s[start] == s[end]:
                start -=1
                end +=1
            return s[start+1:end]
                    
        self. s = s
        result = ''
        for i in range(len(s)):
            palindrome1 = valid_palindrome(s,i,i)
            palindrome2 = valid_palindrome(s,i,i+1)
            result = max([result, palindrome1, palindrome2], key = lambda x:len(x))
        return result
 
