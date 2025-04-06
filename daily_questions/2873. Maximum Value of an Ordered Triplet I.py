"""
You are given a 0-indexed integer array nums.

Return the maximum value over all triplets of indices (i, j, k) such that i < j < k. If all such triplets have a negative value, return 0.

The value of a triplet of indices (i, j, k) is equal to (nums[i] - nums[j]) * nums[k].

"""
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # if len(nums) < 3:
        #     return 0
        # i = 0
        # totalVal = 0
        # while (i < len(nums)-2):
        #     j = i + 1
        #     while (j < len(nums)-1):
        #         k = j + 1
        #         while (k < len(nums)):
        #             if nums[i] > nums[j]:
        #                 tripleVal = (nums[i] - nums[j]) * nums[k]
        #                 totalVal = max(totalVal, tripleVal)
        #             k+=1
        #         j += 1
        #     i+=1
        # return totalVal
        res = 0
        currMax = 0
        diffMax = 0
        for i in range(len(nums)):
            res = max(res, diffMax * nums[i])
            diffMax = max(diffMax, currMax - nums[i])
            currMax = max(currMax, nums[i])
        return res
        
