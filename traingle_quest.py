#import functools
for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    #print(functools.reduce(lambda x,y: (x*10+y),[i]*i))
    print((10**(i)//9)*i)
