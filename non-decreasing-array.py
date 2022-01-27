class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        self.nums = nums
        cnt = 0
        for i in range (len(nums)-1):
            if nums[i] > nums[i+1]:
                cnt +=1
                if i == 0:
                    nums[i] = nums[i+1]
                elif nums[i-1] <= nums[i+1]:
                    nums[i] = nums[i-1]
                else:
                    nums[i+1] = nums[i]
        return False if cnt > 1 else True
