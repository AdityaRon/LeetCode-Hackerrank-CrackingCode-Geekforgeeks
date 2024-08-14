class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        maxNum = float(-inf)
        maxScore = 0
        for num in nums:
            if num > maxNum:
                maxNum = num
        for i in range(1,k+1):
            print(maxNum, i)
            maxScore += maxNum
            maxNum += 1
        return maxScore
        
