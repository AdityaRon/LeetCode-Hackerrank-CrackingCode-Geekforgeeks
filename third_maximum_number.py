class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        self.nums = nums
        firstMax = float("-inf")
        secondMax = float("-inf")
        thirdMax = float("-inf")
        for i in nums:
            if i > firstMax:
                firstMax,secondMax, thirdMax = i, firstMax, secondMax
            elif i > secondMax and i != firstMax:
                secondMax, thirdMax = i, secondMax
            elif i > thirdMax and i != secondMax and i != firstMax:
                thirdMax = i
        print(thirdMax)
        return thirdMax if thirdMax != float('-inf') else firstMax
#         tempNums = list(set(nums))
#         tempNums.sort(reverse=True)
#         if len(tempNums) >= 3:
#             return tempNums[2]
#         else:
#             return tempNums[0]
            
            
            
