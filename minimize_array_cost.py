def minimize_array_cost(n: List[int])-> int:
    #define first and second index
    firstIndex = 0
    secondIndex = 0
    #define max cost
    maxDiff = 0
    minCost = 0
    for i in range(len(n)-1):
        current = n[i]
        next = n[i+1]
        if abs(next-current) > maxDiff:
            maxDiff = abs(next-current)
            firstIndex = i
            secondIndex = i+1
    midPoint = (n[firstIndex] + n[secondIndex])//2
    minCost +=  (n[firstIndex] - midPoint)*(n[firstIndex] - midPoint)
    minCost +=  (n[secondIndex] - midPoint)*(n[secondIndex] - midPoint)
    for i in range(len(n)-1):
        if i == firstIndex:
            continue
        minCost += (n[i] - n[i+1])*(n[i] - n[i+1])
    return minCost
