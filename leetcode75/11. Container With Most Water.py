# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

class Solution:
    def maxArea(self, height: List[int]) -> int:
      self.height = height
      start  = 0 
      end = len(height)-1
      maxArea = 0
      while start != end:
        if height[start] > height[end]:
          currentArea = height[end] * (end-start)
          maxArea = max(maxArea, currentArea)
          end -=1
        else:
          currentArea = height[start]*(end-start)
          maxArea = max(maxArea, currentArea)
          start +=1
      return maxArea
          
