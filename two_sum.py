class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.nums = nums
        self.target = target
        diff1 = {}
        for i in nums:
            diff1[i] = target - i
        print(diff1)
        for i,j in diff1.items():
            if i!=j:
                if i in nums:
                    if j in nums:
                        return(nums.index(i), nums.index(j))
                        break
            else:
                if i in nums:
                    if j in nums:
                        a = nums.index(i)
                        nums.remove(i)
                        b = nums.index(j)
                        return(a,b+1)
                        break
        
            
