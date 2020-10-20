class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        self.paragraph = paragraph
        self.banned = banned
        frequency = {}
        import re
        paragraph = re.sub(r'[^\w\s]', ' ', paragraph.lower())
        for i in paragraph.split():
            frequency[i] = frequency.get(i,0) + 1
        for i in sorted(frequency, key=frequency.get, reverse=True):
            if i not in banned:
                return i
           
    #alternative solution    
    def mostCommonWord(self, p, banned):
        ban = set(banned)
        words = re.findall(r'\w+', p.lower())
        return collections.Counter(w for w in words if w not in ban).most_common(1)[0][0]
            
        
