class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        self.A = A
        self.B = B
        from collections import Counter
        #print(A.split(' '))
        # Adict = Counter(A.split(' '))
        # Bdict = Counter(B.split(' '))
        # result = []
        # for i,j in Adict.items():
        #     if j == 1:
        #         if i not in Bdict.keys():
        #             result.append(i)
        # for i,j in Bdict.items():
        #     if j == 1:
        #         if i not in Adict.keys():
        #             result.append(i)
        # return result
        Stringdict = Counter(A.split(' ') + B.split(' '))
        result = [key for key, value in Stringdict.items() if value == 1]
        return result
            
                    
        
