#nums = [1, 2, 5, 2, 1]
# nums = [3, 1, 9, 2]
def equality(num: list) -> list:
    for i,j in enumerate(nums):
#         print(i, nums[0:i])
        if sum(nums[0:i]) == sum(nums[i+1:]):
            return i
    return -1
