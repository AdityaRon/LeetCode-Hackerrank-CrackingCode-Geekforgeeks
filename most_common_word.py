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
            
        
            
        
