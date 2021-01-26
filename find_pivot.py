class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        self.nums = nums
        left = 0
        right = sum(nums)
        for i, j in enumerate(nums):
            right -= j
            if left == right:
                return i
            left += j
        return -1
            
        
