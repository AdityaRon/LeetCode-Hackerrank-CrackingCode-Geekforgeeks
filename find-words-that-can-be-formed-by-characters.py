class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        import collections 
        self.words = words
        self.chars = chars
        charcounter = collections.Counter(chars)
        strings = []
        result = 0
        for word in words:
            results = 0
            wordcounter = collections.Counter(word)
            for i,j in wordcounter.items():
                if wordcounter[i] <= charcounter.get(i, 0):
                    print(i)
                    results +=1
                else:
                    results = 0
                    break
            if results !=0:
                strings.append(word)
        for i in strings:
            result += len(i)
        return(result)
