class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        from itertools import combinations
        results = []
        for i in range(1,len(nums)+1):
            results += list(combinations(nums,i))
        return results + [[]]
