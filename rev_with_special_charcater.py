def rev(str):
    temp = []
    for i in str:
        if i.isalpha():
            temp.append(i)
        temp = temp[::-1]
    liststr = list(str)
    for i,j in enumerate(liststr):
        if j.isalpha():
            liststr[i] = temp.pop(0)
    return ''.join(liststr)