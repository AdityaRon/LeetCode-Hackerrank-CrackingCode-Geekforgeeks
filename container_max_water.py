class Solution:
    def maxArea(self, height: List[int]) -> int:
        self.height = height
        results = 0
        # for i,j in enumerate(height):
        #     for k,l in enumerate(height[i:]):
        #         results = max(results, min(j,l)*k)
        # return results
        p1 = 0  # first (left) pointer
        p2 = len(height) - 1  # second (right) pointer
        area = 0
        while p1 != p2:
            if height[p1] > height[p2]:
                area = max(area,height[p2] * (p2 - p1))  # height of smaller edge multiplies on length
                p2 -= 1  # changing smaller edge
            else:
                area = max(area,height[p1] * (p2 - p1))
                p1 += 1
        return area
        
