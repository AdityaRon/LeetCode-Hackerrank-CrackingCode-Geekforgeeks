import sys
def gemstones(arr):
    s = ''
    u = ''
    t = {}
    count = 0
    for i in arr:
        s += str(set(i))
        u += str(i)
    p = set(u)
    for i in p:
        t[i] = s.count(i)
    for k in t.values():
        if k == n:
            count+=1
    return count
n = int(input().strip())
arr = []
arr_i = 0
for arr_i in range(n):
    arr_t = str(input().strip())
    arr.append(arr_t)
result = gemstones(arr)
print(result)

##alternate-version
rocks = [set(input()) for _ in range(int(input()))]
print(rocks)
gems = set.intersection(*rocks)
print(gems)
print(len(gems))