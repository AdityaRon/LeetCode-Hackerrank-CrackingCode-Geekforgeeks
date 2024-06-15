class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
    
        #print(nums[0], nums[1:])
        if len(nums) == 1 :
            return 0 
        elif sum(nums[1:]) == 0:
            return 0
        # elif sum(nums[:len(nums)-1]) == 0:
        #     return len(nums)-1
        for index, value in enumerate(nums):
            left_half = nums[0:index]
            right_half = nums[index+1:]
            #print(left_half, right_half)
            if sum(left_half) == sum(right_half):
                return index
        return -1
