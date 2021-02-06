class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        self.candies = candies
        self.num_people = num_people
        ans = [0] * num_people
        i = 0
        while candies > 0:
            ans[(i % num_people)] += min(candies, i+1)
            i+=1
            candies -= i
        return ans
