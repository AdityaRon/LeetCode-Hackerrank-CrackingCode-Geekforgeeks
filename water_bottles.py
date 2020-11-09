class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        self.numBottles = numBottles
        self.numExchange = numExchange
        ans = r = 0
        while numBottles:
            ans += numBottles
            numBottles, r = divmod(numBottles + r, numExchange)
        return ans 
