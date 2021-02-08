class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        self.arr = arr
        result = []
        for i in arr:
            result.append((bin(i).count("1"), i))
        sorted_result = sorted(result, key = lambda x: (x[0],x) )
        print(sorted_result)
        return ([i[1] for i in sorted_result])
        
