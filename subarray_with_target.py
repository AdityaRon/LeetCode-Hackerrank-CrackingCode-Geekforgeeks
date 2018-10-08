def maximum_sub_array(arr,n,target):
    cursum = arr[0]
    start = 0
    i=1
    while(i<=n):
        if cursum > target and start < i-1:
            cursum = cursum - arr[start]
            start +=1
        if cursum == target:
            return(start, i-1)
            #return 1
        if i < n:
            cursum = cursum + arr[i]
        i+=1
    return (0)
