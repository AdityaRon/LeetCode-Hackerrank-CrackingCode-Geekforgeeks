class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        self.nums = nums
        self.k = k
        targets = {}
        for i,j in enumerate(nums):
            if j in targets and abs(targets[j] - i) <= k:
                return True
            targets[j] = i
        return False
                
        
