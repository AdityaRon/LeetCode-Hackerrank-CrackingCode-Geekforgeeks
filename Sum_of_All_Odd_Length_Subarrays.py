class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        self.arr = arr
        result = 0
        length = len(arr)
        if len(arr) % 2 != 0:
            result += sum(arr)*2
        if len(arr) % 2 == 0:
            result += sum(arr)
        odds = []
        for i in range(2,length):
            if i % 2 != 0:
                odds.append(i)
        for i in odds:
            j= 0
            while i<=len(arr):
                print(arr[j:i])
                result += sum(arr[j:i])
                j+=1
                i+=1
        return(result) if len(arr) > 2 else sum(arr)
