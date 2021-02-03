c = ['A', 'B', 'C', 'D'] # list of categories
l = [20, 15, 35, 30]
l = [i/sum(l) for i in l]
# temp = 0.2
# for i in range(1,len(l)):
#     l[i] = l[i] + temp
#     temp = l[i]
l = [sum(l[:i]) for i in range(1,len(l)+1)]
print(l)
def random_generator(c,l):
    import random
    num = random.uniform(0,1)
    for i,j in zip(c,l):
        if num <= j:
            return (i)
