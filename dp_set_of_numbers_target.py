def count_array(array, results, target, index):
    key = str(target) + ':' + str(index)
    if key in results:
        return results[key]
    elif target == 0:
        return 1
    elif target < 0:
        return 0
    elif index < 0:
        return 0
    elif array[index] > target:
        result = count_array(array, results, target, index-1)
    else:
        result = count_array(array, results, target-array[index], index-1) + count_array(array, results, target, index-1)
    results[key] = result
    return result
