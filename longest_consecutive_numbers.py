class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        self.nums  = nums
        if len(nums) == 0:
            return 0
        count = 1
        maxCount = 1
        nums = list(set(nums))
        nums.sort()
        temp = nums[0]
        for i in nums[1:]:
            if temp + 1 == i:
                count +=1
                maxCount = max(count, maxCount)
            else:
                count = 1
            temp = i
        return maxCount


//Without sorting

# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         uniques = set(nums)
#         max_length = 0

#         while uniques:
#             low = high = uniques.pop()
            
#             while low - 1 in uniques or high + 1 in uniques:
#                 if low - 1 in uniques:
#                     uniques.remove(low - 1)
#                     low -= 1
                
#                 if high + 1 in uniques:
#                     uniques.remove(high + 1)
#                     high += 1

#             max_length = max(high - low + 1, max_length)

#         return max_length

        
