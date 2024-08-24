# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
# frequency
#  of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

# Example 1:

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# Example 2:

# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# Example 3:

# Input: candidates = [2], target = 1
# Output: []

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # from itertools import combinations_with_replacement
        # all_combs = []
        # result = []
        # n = (target // min(candidates) + 1)
        # for i in range(n):
        #     combinations = combinations_with_replacement(candidates, i)
        #     for comb in combinations:
        #         all_combs.append(list(comb))
        # for combination in all_combs:
        #     #print(sum(combination))
        #     if sum(combination) == target:
        #         result.append(combination)
        # #print(all_combs)
        # return result
        # results = []
        # total = 0
        # def dfs(i, current, total):
        #     if total == target:
        #         results.append(current.copy())
        #         return 
        #     if  i >= len(candidates) or total > target:
        #         return 
        #     current.append(candidates[i])
        #     dfs(i, current, total+candidates[i])
        #     current.pop()
        #     dfs(i+1, current, total)

        # dfs(0, [], total)

        # return results
        result, solution = [], []
        def dfs(start, total, solution):                                                 
            if total == target:
                result.append(solution.copy())
                return 
            if start >= len(candidates) or total > target:
                return
            solution.append(candidates[start])
            dfs(start, total + candidates[start], solution)
            solution.pop()
            dfs(start+1, total, solution)

        dfs(0, 0, solution)
        return result
