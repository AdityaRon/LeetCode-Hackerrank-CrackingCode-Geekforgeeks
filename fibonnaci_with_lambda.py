cube = lambda x: x**3

def fibonacci(n):
    # return a list of fibonacci numbers
    count = 1
    result = [0]
    a,b = 0,1
    while count < n:
        a, b = b, a+b
        result.append(a)
        count +=1
    return result if n > 0 else []

if __name__ == '__main__':
