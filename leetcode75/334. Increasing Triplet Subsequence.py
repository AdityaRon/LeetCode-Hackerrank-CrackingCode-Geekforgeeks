class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        # for i in range(0, len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             if nums[i] < nums[j] < nums[k]:
        #                 return True
        #             k+=1
        #         j+=1
        #     i+=1
        # return False
        smallest = float('inf')
        second_smallest = float('inf')
        for num in nums:
            if num <= smallest:
                smallest = num
            if num <= second_smallest and num > smallest:
                second_smallest = num
            if num > smallest and num > second_smallest:
                return True
        return False

        
