class Solution:
    def rob(self, nums: List[int]) -> int:
        self.nums = nums
        if len(nums) > 0:
            memo = [0]* (len(nums) + 1) 
            memo[0] = 0
            memo[1] = nums[0]
            for i in range(1, len(nums)):
                current = nums[i]
                memo[i+1] = max(memo[i], memo[i-1]+ current)
            return memo[-1]
        else:
            return 0
