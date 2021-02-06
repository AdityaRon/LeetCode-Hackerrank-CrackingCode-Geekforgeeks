class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        self.nums = nums
        self.k = k
        # result = []
        # for i,j in enumerate(nums):
        #     if j == 1:
        #         result.append(i)
        # if len(result) > 0:
        #     temp = result[0]
        #     for i in result[1:]:
        #         if abs(i-temp-1) < k:
        #             return False
        #         temp = i
        #     return True
        # else:
        #     return True
        # previousIndex = 0
        # for i, j in enumerate(nums):
        #     if previousIndex != 0:
        #         if j ==0:
        #             continue
        #         elif j == 1 and (i - previousIndex-1) >= k:
        #             previousIndex = i
        #         else:
        #             return False
        #     else:
        #         previousIndex = i
        #         continue
        # return True
        previousIndex = -1
        for i in range(len(nums)):
            if nums[i] == 1:
                if previousIndex != -1 and (i-previousIndex-1) < k:
                    # print(previousIndex)
                    return False
                previousIndex = i
        return True
                
                
