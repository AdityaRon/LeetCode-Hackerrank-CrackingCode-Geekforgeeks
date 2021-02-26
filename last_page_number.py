#assuming the page numbers are less than 99. Scaling this will be problem.
def last_page_number(a:str) -> int:
    i = 1
    temp = int(a[0])
    while i <= len(a)-1:
        #print(i, temp, a[i:i+2])
        if temp < 9 and int(a[i]) == temp + 1 :
            temp = int(a[i])
        elif temp >= 9 and int(a[i:i+2]) == temp + 1:
            temp = int(a[i:i+2])
            i+=1
        else:
            break
            return temp
        i+=1
    return temp
