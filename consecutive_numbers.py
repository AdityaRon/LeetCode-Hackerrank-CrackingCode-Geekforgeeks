def consecutive_numbers(n):
    result = []
    for i in range(1, n+1):
        total = 0
        intermediate = []
        while total < n:
            total += i
            intermediate.append(i)
            i+=1
        if total == n:
            result.append(intermediate)
    return result
            
