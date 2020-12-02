class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        self.accounts = accounts
        # result = 0
        # for i in accounts:
        #     result = max(result, sum(i))
        # return result
        return max(map(sum, accounts))
        
