class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        start = nums[0]
        end = nums[0]
        result = []
        for i in nums[1:]:
            if i == end + 1:
                end = i
            elif start == end:
                result.append(str(start))
                start = i
                end = i
            else:
                result.append(f"{start}->{end}")
                start = i
                end = i
        if start == end:
            result.append(str(start))
        else:
            result.append(f"{start}->{end}")
        return result
        
