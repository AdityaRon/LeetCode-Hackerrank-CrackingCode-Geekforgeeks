class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        if len(set(nums)) == 1:
            return False
        previous = nums[0]
        for current in nums[1:]:
            if previous == current:
                return False
            if previous % 2 == 0 and current % 2 == 0:
                return False
            if previous % 2 != 0 and current % 2 != 0:
                return False
            previous = current
        return True

        
