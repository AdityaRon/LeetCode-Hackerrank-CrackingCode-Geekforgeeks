class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        self.nums = nums
        maps = {}
        maxi = max(nums, default = 0)
        for num in nums:
            maps[num] = True
        print(maps, maxi)
        for i in range(1, maxi):
            if i not in maps:
                return i
        return 1 if maxi < 0 else maxi+1
        # for i in range(1, len(nums)):
        #     if i not in set(nums):
        #         return i
        # return max(nums)+1 if max(nums) > 0 else 1
