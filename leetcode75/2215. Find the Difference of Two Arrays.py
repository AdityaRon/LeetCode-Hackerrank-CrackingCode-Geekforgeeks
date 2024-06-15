class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        result1 = []
        result2 = []
        finalResult = []
        for i in nums1:
            if i not in nums2 and i not in result1:
                result1.append(i)
        for i in nums2:
            if i not in nums1 and i not in result2:
                result2.append(i)
        finalResult.append(result1)
        finalResult.append(result2)
        return finalResult
