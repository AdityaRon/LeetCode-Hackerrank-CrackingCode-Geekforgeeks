def max_product_array(arr):
    maxprod = arr[0] 
    minprod = arr[0]
    maxarray = arr[0]
    for i in arr[1:]:
        minprod,maxprod = min(i, i * maxprod, i * minprod), max(i, i * maxprod, i * minprod)
        maxarray = max(maxarray,maxprod)
    return (maxprod)
