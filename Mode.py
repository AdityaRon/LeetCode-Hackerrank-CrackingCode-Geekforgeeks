import sys
from collections import Counter

n = int(input().strip())
types = list(map(int, input().strip().split(' ')))
# your code goes here
b = Counter(types).most_common()
h = (0,0)
for i in b:
    if i[1] > h[1]:
        h = i
    elif i[1] == h[1]:
        if i[0] < h[0]:
            h = i
    elif i[1] < h[1]:
        break
print(h[0])
