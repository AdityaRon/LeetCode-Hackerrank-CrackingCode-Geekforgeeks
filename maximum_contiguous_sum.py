def maximum_sum(arr):
    cursum = maxsum = arr[0]
    i=1
    n=len(arr)-1
    while(i<=n):
        cursum += arr[i]
        cursum = max(i,cursum)
        maxsum = max(cursum,maxsum)
        i+=1
    return(maxsum)

##alternative solution
from sys import maxint
def maximum_sum(arr):
    cursum = -maxint - 1
    maxsum = 0
    for i in arr:
        cursum = maxsum + i
        if maxsum < cursum:
            maxsum = cursum
        if cursum < 0:
            cursum = 0
    return(maxsum)
