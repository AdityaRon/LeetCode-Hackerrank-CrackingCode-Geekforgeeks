class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        self.nums1 = nums1
        self.nums2 = nums2
        result = [-1] * len(nums1)
        for i,j in enumerate(nums1):
            if j in nums2:
                temp = nums2.index(j)
                #print(temp)
                while  temp <= len(nums2)-2:
                    if nums2[temp+1] >= j:
                        result[i] = nums2[temp+1]
                        break
                    temp = temp+1
        return result
            
            
            
            
        
