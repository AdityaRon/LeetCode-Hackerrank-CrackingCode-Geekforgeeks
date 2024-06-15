class Solution:
    def countBits(self, n: int) -> List[int]:
        bitCount = []
        for i in range(0, n+1):
            temp = bin(i)
            nonzero = temp.count('1')
            bitCount.append(nonzero)
        return bitCount     
