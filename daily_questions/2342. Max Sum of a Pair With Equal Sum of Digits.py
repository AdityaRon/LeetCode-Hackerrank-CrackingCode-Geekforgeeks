```
You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].

Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.

 

Example 1:

Input: nums = [18,43,36,13,7]
Output: 54
Explanation: The pairs (i, j) that satisfy the conditions are:
- (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
- (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
So the maximum sum that we can obtain is 54.
Example 2:

Input: nums = [10,12,19,14]
Output: -1
Explanation: There are no two numbers that satisfy the conditions, so we return -1.```

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def sum_of_digits(num):
            total = 0
            for i in str(num):
                total += int(i)
            return total
        # i = 0
        # tmpSum, maxSum = 0, 0
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if sum_of_digits(nums[i]) == sum_of_digits(nums[j]):
        #             tmpSum = nums[i] + nums[j]
        #             maxSum = max(maxSum, tmpSum)
        # return maxSum if maxSum > 0 else -1
        groups = {}
        for num in nums:
            temp = sum_of_digits(num)
            if temp not in groups:
                groups[temp] = [num]
            else:
                groups[temp].append(num)
        #maxSum = max([key for key in groups.keys()])
        result = 0
        print(groups)
        #print(maxSum)
        for key, value in groups.items():
            if len(value) >= 2:
                tmpSum = sum(sorted(value, reverse=True)[0:2])
                result = max(tmpSum, result)
        return result if result > 0 else -1
        
