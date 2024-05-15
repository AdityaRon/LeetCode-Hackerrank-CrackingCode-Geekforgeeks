class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        self.candies = candies
        self.extraCandies = extraCandies
        result = []
        maxCandy = max(candies)
        for i in candies:
            if i + extraCandies >= maxCandy:
                result.append(True)
            else:
                result.append(False)
        return result
        
