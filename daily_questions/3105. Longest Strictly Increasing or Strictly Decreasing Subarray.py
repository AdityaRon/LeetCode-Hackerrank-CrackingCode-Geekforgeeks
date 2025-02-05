"""
You are given an array of integers nums. Return the length of the longest 
subarray
 of nums which is either 
strictly increasing
 or 
strictly decreasing
.

 

Example 1:

Input: nums = [1,4,3,3,2]

Output: 2

Explanation:

The strictly increasing subarrays of nums are [1], [2], [3], [3], [4], and [1,4].

The strictly decreasing subarrays of nums are [1], [2], [3], [3], [4], [3,2], and [4,3].

Hence, we return 2.

Example 2:

Input: nums = [3,3,3,3]

Output: 1

Explanation:

The strictly increasing subarrays of nums are [3], [3], [3], and [3].

The strictly decreasing subarrays of nums are [3], [3], [3], and [3].

Hence, we return 1.

Example 3:

Input: nums = [3,2,1]

Output: 3

Explanation:

The strictly increasing subarrays of nums are [3], [2], and [1].

The strictly decreasing subarrays of nums are [3], [2], [1], [3,2], [2,1], and [3,2,1].

Hence, we return 3.
"""
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        # increaseSeq = 1
        # decreaseSeq = 1
        # subincreaseSeq = 1
        # subdecreaseSeq = 1
        # for i in range(len(nums)-1):
        #     if nums[i] > nums[i+1]:
        #         subincreaseSeq += 1
        #     else:
        #         increaseSeq = max(increaseSeq,subincreaseSeq)
        #         subincreaseSeq = 1
        #     increaseSeq = max(increaseSeq,subincreaseSeq)
        # for i in range(len(nums)-1):
        #     if nums[i] < nums[i+1]:
        #         subdecreaseSeq += 1
        #     else:
        #         decreaseSeq = max(decreaseSeq,subdecreaseSeq)
        #         subdecreaseSeq = 1
        #     decreaseSeq = max(decreaseSeq,subdecreaseSeq)
        # return max(increaseSeq, decreaseSeq)
        increaseSeq, decreaseSeq, maxSeq = 1,1,1
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                increaseSeq += 1
                decreaseSeq = 1
            elif nums[i] < nums[i+1]:
                decreaseSeq += 1
                increaseSeq = 1
            else:
                increaseSeq = 1
                decreaseSeq = 1
            maxSeq = max(maxSeq, increaseSeq, decreaseSeq)

        return maxSeq
        
