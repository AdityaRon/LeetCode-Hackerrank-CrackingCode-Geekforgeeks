class Solution:
    def findLucky(self, arr: List[int]) -> int:
        self.arr = arr
        from collections import Counter
        results = Counter(arr)
        #results  = OrderedDict(sorted(results.items(), key=lambda t: t[0], reverse=True))
        #print(results)
        # for i in results:
        #     if i == results[i]:
        #         return i
        #     else:
        #         continue
        # return -1
        return max([i for i,j in results.items() if i==j]+[-1])
