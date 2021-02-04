class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        self.words = words
        words = sorted(words, key=len)
        results = []
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if words[i] in words[j]:
                    results.append(words[i])
                    break
        return results
                    
