class Solution:
    def canJump(self, nums: List[int]) -> bool:
        self.nums = nums
        target = len(nums)-1
        m = 0
        i = len(nums)-2
        while (i >= 0):
            if nums[i] + i >= target:
                target = i
            i-=1
        return target == 0

        
