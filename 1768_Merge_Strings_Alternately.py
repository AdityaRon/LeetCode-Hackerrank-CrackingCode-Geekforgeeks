class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        for i,j in zip(word1, word2):
            result += i
            result += j
        if len(word2) > len(word1):
            result += word2[len(word1) : len(word2)]
        elif len(word1) > len(word2):
            result += word1[len(word2) : len(word1)]
        return result
