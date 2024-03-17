#525. Contiguous Array
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zeros, ones = 0, 0
        result = 0
        diff_index = {}
        for index, number in enumerate(nums):
            if number == 0:
                zeros += 1
            else:
                ones += 1
            if ones-zeros not in diff_index:
                diff_index[ones-zeros] = index
            if ones == zeros:
                result = index + 1
            else:
                result = max(result, index -  diff_index[ones-zeros])
            #print(diff_index)
        return result
