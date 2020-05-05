class Solution:
    def isHappy(self, n: int) -> bool:
        self.n = n
        results = set()
        while n != 1:
            summed = 0
            for i in str(n):
                summed += int(i)*int(i)
            if summed not in results:
                results.add(n)
            else:
                return False
            n = summed
        return True 
            
