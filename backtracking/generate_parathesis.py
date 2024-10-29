# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]
 

# Constraints:

# 1 <= n <= 8


class Solution:
   def generateParenthesis(self, n: int) -> List[str]:
        # from itertools import permutations
        # parentheses = ['('] * n + [')'] * n
        # all_perms = list(set(permutations(parentheses)))
        # def is_valid(perm):
        #     balance = 0
        #     for char in perm:
        #         if char == '(':
        #             balance += 1
        #         else:
        #             balance -=1
        #         if balance < 0:
        #             return False
        #     return balance == 0
        # result = ["".join(perm) for perm in all_perms if is_valid(perm)]
        # return result
        ans, sol = [], []
        def dfs(opens, closes):
            if len(sol) == 2 * n:
                ans.append(''.join(sol.copy()))
                return 
            if opens < n:
                sol.append('(')
                dfs(opens + 1, closes)
                sol.pop()
            if opens > closes:
                sol.append(')')
                dfs(opens, closes +1)
                sol.pop()
        dfs(0,0)
        return ans
