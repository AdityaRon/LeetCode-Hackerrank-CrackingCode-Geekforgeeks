class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        self.text = text
        from collections import Counter
        compare = Counter('balloon')
        ballon = Counter(text)
#         result = []
#         for i in compare.keys():
#             result.append((ballon[i]//compare[i]))
#         return min(result)
        return min([ballon[i]//compare[i] for i in compare.keys()])
            
            
            
        
            
        
