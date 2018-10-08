def maximum_sum(arr):
    cursum = maxsum = arr[0]
    i=1
    n=len(arr)-1
    while(i<=n):
        cursum += arr[i]
        cursum = max(0,cursum)
        maxsum = max(cursum,maxsum)
        i+=1
    return(maxsum)
