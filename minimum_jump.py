def avoidObstacles(inputArray):
    jump = 1
    obstacle = True
    array = sorted(inputArray)
    while(obstacle):
        obstacle = False
        jump+=1
        for i in range(0, len(array)):
            if array[i] % jump == 0:
                obstacle = True
                break
    return jump
    
