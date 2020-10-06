#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    arr1 = sorted(arr)
    swaps = 0
    while arr != arr1:
        for i,j in enumerate(arr):
            if i == j-1:
                continue
            arr[j-1], arr[i] = arr[i], arr[j-1]
            swaps +=1
            if arr == arr1:
                break
    return swaps
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
