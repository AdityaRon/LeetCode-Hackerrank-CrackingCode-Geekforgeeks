def max_sub_array_length(nums,k):
    
    result = {}
    result[0] = -1
    target = 0
    subarray = 0
    for i,j in enumerate(nums):
        target += j
        if target - k in result.keys():
            subarray = max(subarray, i-result[target-k])
        if target not in result:
            result[target] = i
    return subarray
