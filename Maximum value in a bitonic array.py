T = int(input())
for i in range(0,T):
    N = int(input())
    array = list(map(int, input().split()))
    j = 0
    key = 0
    while (j < N-1):
        temp = array[j] - array[j+1]
        if temp > 0:
            key = array[j]
            print(array[j])
            break
        elif temp == 0:
            key = array[j]
            print(array[j])
            break
        j+=1
    if key == 0:
       print(array[N-1])
       
       
       
# Constraints:

# 1 ≤ T ≤ 50
# 3 ≤ N ≤ 100
# 1 ≤ a[i] ≤ 100000


# Example:

# Input
# 2
# 9
# 1 15 25 45 42 21 17 12 11
# 5
# 1 45 47 50 5

# Output
# 45
# 50
