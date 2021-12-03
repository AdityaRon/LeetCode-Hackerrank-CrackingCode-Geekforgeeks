# Let's walk up from left to right until we can't: that has to be the peak. We should ensure the peak is not the first or last element. Then, we walk down. If we reach the end, the array is valid, otherwise its not.

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        totalLength = len(arr)
        i = 0
        while i+1 < totalLength and arr[i] < arr[i+1]:
            i+=1
        if i == 0 or i == totalLength-1:
            return False
        while i+1 < totalLength and arr[i] > arr[i+1]:
            i+=1
        return i == totalLength-1
