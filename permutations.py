class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        results = []
        import itertools
        # strnums = ''.join(map(str,nums))
        permutations = itertools.permutations(nums)
        for i in permutations:
            results.append(i)
        return results
        
