# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for i in range(n):
    from collections import deque
    length, cube = int(input()), deque(map(int, input().split()))
    # print(cube)
    cube_reversed = sorted(cube,reverse=True)
    for i in cube_reversed:
        if i == cube[-1]:
            cube.pop()
        elif i == cube[0]:
            cube.popleft()
        else:
            print('No')
            break
    else:
        print('Yes')
        
