```
You are given a 0-indexed integer array nums, and an integer k.

You are allowed to perform some operations on nums, where in a single operation, you can:

Select the two smallest integers x and y from nums.
Remove x and y from nums.
Insert (min(x, y) * 2 + max(x, y)) at any position in the array.
Note that you can only apply the described operation if nums contains at least two elements.

Return the minimum number of operations needed so that all elements of the array are greater than or equal to k.
```


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        def some_operation(a,b):
            return  ( (min(a,b) * 2) + max(a, b))
        import heapq
        results = []
        count_of_ops = 0
        for num in nums:
            if num < k:
                heapq.heappush(results, num)
        if len(results) == 1:
            return 1
        if len(results) == 0:
            return 0
        #print(results)
        while results[0] < k:
            a = heapq.heappop(results)
            if len(results) == 0:
                return count_of_ops + 1
            b = heapq.heappop(results)
            heapq.heappush(results, some_operation(a,b))
            count_of_ops += 1
        return count_of_ops
