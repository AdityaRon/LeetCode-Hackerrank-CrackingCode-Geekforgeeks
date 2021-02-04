class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        self.code = code
        self.k = k
        codeUpdated = code * 2
        result = []
        if k == 0:
            return [0] * len(code)
        elif k > 0:
            for i in range(0,len(code)):
                result.append(sum(codeUpdated[i+1:i+1+k]))
        else:
            for i in range(len(code), len(code)*2):
                result.append(sum(codeUpdated[i+k:i]))
        return result
                
