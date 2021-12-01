# candies = 8
# exchange = 9
def eat_candies(x,y):
    if x < y:
        return x
    elif x == y:
        return x + 1
    else:
        additional = 0
        temp = x
        while temp >= y:
            temp = temp - y
            additional +=1
        return candies + additional
        
eat_candies(8, 9)
