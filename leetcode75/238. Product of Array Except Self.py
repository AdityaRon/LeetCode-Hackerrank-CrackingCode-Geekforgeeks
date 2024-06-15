class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        self.nums = nums
        # results = []
        # start = 0
        # end = len(nums)
        # for index, value in enumerate(nums):
        #     start = index
        #     result = 1
        #     for j in nums[(start+1):end]:
        #         result *= j
        #     for j in nums[0:start]:
        #         result *= j
        #     results.append(result)
        # return results
        left_array = [0]*len(nums)
        right_array = [0]*len(nums)
        results = []
        left_array[0] = 1
        right_array[len(right_array)-1] = 1
        for i in range(1, len(nums)):
            left_array[i] = left_array[i-1] * nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            right_array[i] = right_array[i+1] * nums[i+1]
        print(left_array)
        print(right_array)
        for i,j in zip(left_array, right_array):
            results.append(i*j)
        return results

