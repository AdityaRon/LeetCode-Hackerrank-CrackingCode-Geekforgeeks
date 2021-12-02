# Given an integer array, nums, for each nums[i] you need to find the number of elements that are strictly smaller than it. Do this for all values in the array and return the result in an array

# nums = [4, 2, 9, 10, 3]
# ans = [2, 0, 3, 4, 1]
def smallerItems(nums: list) -> list:
    sortedNums = sorted(nums)
    results = []
    for i in nums:
        results.append(sortedNums.index(i))
    return results
