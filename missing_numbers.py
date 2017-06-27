len1 = int(input())
list1 = list(map(int,input().split()))
len2 = int(input())
list2 = list(map(int,input().split()))
def missing(a,b):
    c = max(a+b)
    zeros =[]
    for i in range(c+1):
        zeros.append(0)
    for i in a:
        zeros[i] +=1
    for j in b:
        zeros[j] -=1
    for i in range(len(zeros)):
        if zeros[i] !=0:
            print(i, end=' ')
missing(list1, list2)
        
