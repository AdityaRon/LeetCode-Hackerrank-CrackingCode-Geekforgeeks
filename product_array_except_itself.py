class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_array = [0]* len(nums)
        right_array = [0] * len(nums)
        left_array[0] = 1
        right_array[len(right_array)-1] = 1
        result = []
        for i in range(1,len(nums)):
            left_array[i] = left_array[i-1]*nums[i-1]
        for j in range(len(nums)-2, -1, -1):
            right_array[j] = right_array[j+1]*nums[j+1]
        for i,j in zip(left_array, right_array):
            result.append(i*j)
        return result
