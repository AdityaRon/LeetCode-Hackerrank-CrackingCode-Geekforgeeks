# Given an integer array nums that may contain duplicates, return all possible 
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        nums.sort()
        results, solution = [], []
        results, solution = [], []
        def dfs(start, combination):
            if start >= len(nums):
                results.append(combination.copy())
                return 
            combination.append(nums[start])
            dfs(start+1, combination)
            combination.pop()
            #skip duplicates
            while start + 1 < len(nums) and nums[start] == nums[start+1]:
                start += 1
            dfs(start+1, combination)
        dfs(0, [])
        return results
        
