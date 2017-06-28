import sys


h = list(map(int, input().strip().split(' ')))
word = input().strip()
length = len(word)
tallest = {}
j = 97
for i in h:
    tallest[chr(j)] = i
    j+=1
highest = 0
for i in word:
    if tallest[i] > highest:
        highest = tallest[i]
print(highest*length)
    
