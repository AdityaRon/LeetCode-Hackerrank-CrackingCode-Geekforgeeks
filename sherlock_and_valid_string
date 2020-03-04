#!/bin/python3

import math
import os
import random
import re
import sys
import collections

# Complete the isValid function below.
def isValid(s):
    stringDict = collections.Counter(s)
    if len(set(stringDict.values())) == 1:
        return 'YES'
    elif len(set(stringDict.values())) > 2:
        return 'NO'
    else:
        minimum = min(stringDict.values())
        maximum = max(stringDict.values())
        values = list(stringDict.values())
        if values.count(minimum) == 1:
            return 'YES'
        if values.count(maximum) > 1 or maximum - minimum > 1:
            return 'NO'
        return 'YES'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
