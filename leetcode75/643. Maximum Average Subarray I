class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # start = 0
        # end = k
        # maxAvg = -999999
        # if len(nums) == 0:
        #     return 0
        # elif len(nums) == 1:
        #     return nums[0]
        # elif k == 1:
        #     return max(nums)
        # while start  <= len(nums) - k:
        #     #end = start + end
        #     #print(start, end)
        #     #print(nums[start:end])
        #     tempAvg = sum(nums[start:end]) / k
        #     start += 1
        #     end += 1
        #     maxAvg = max(tempAvg, maxAvg)
        # return maxAvg
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif k == 1:
            return max(nums)
        else:
            currSum = sum(nums[:k])
            maxSum = currSum
            for i in range(k, len(nums)):
                currSum += nums[i] - nums[i-k]
                maxSum = max(currSum, maxSum)
        return maxSum/k
