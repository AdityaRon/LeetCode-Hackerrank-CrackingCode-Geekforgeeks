#!/bin/python3

import sys

def getRecord(s):
    if len(s) == 1:
        return(0,0)
    elif s[0] > s[1]:
        Largest = s[0]
        Smallest = s[1]
        count = 0
        count1 = 1
    elif s[0] == s[1]:
        Largest = s[0]
        Smallest = s[1]
        count = 0
        count1 = 0
    else:
        Largest = s[1]
        Smallest = s[0]
        count = 1
        count1 = 0
    for i in s[2:]:
        if i > Largest:
            count+=1
            Largest = i
    for i in s[2:]:
        if i < Smallest:
            count1+=1
            Smallest = i
    return(count, count1)

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))
