class Solution:
    def trimMean(self, arr: List[int]) -> float:
        self.arr = arr
        numElem = len(arr)
        arr = sorted(arr)
        start = int(numElem*0.05)
        end = int(numElem*0.95)
        #print(numElem,start,end)
        return round(sum(arr[start:end])/len(arr[start:end]), 5)
