class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        denom = sum(w)
        for i in range(len(w)):
            w[i] = w[i]/denom
        for i in range(1,len(w)):
            w[i] += w[i-1]
        print(w)
    def pickIndex(self) -> int:
        import random
        num = random.uniform(0,1)
        for index, weight in enumerate(self.w):
            if num <= weight:
                return index
            
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
