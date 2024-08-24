# Given an integer array nums of unique elements, return all possible 
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results, solution = [], []
        def dfs(start, combination):
            if start >= len(nums):
                results.append(combination.copy())
                return  
            combination.append(nums[start])
            #decision 1 - to include the current num in combination
            dfs(start+1, combination)
            combination.pop()
            # decision 2- to exlcude the current num in combination and move on to next
            dfs(start+1, combination)
        dfs(0, solution)
        return results
           

        
