def areFollowingPatterns(strings, patterns):
    # temp = strings[0]
    # tempPattern = patterns[0]
    # for i,j in zip(strings[1:], patterns[1:]):
    #     if temp == i:
    #         if tempPattern != j:
    #             return False
    #     elif temp != i:
    #         if tempPattern == j:
    #             return False
    #     else:
    #         continue
    #     temp = i
    #     tempPattern = j
    # return True
    dict1 = {}
    dict2 = {}
    for i, (j,k) in enumerate(zip(strings,patterns)):
        p1 = dict1[j] = dict1.get(j,i)
        p2 = dict2[k] = dict2.get(k,i)
        if p1 != p2:
            return False
    return True

