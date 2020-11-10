class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.stones = stones
        while (len(stones) != 1 and len(stones) != 0):
            heavy_1 = max(stones)
            stones.remove(heavy_1)
            heavy_2 = max(stones)
            stones.remove(heavy_2)
            if heavy_1 != heavy_2:
                stones.append(heavy_1-heavy_2)
        return stones[0] if len(stones) !=0 else 0
            
            
