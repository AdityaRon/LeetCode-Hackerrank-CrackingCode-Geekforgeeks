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
        
