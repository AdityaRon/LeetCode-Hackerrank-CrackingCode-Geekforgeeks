def unique_string(s):
    if len(s) == 0:
        return ""
    else:
        temp = s[0]
        for i,j in enumerate(s[1:]):
            if temp == j :
                #print(i)
                s = s[0:i] + s[i+2:]
                #print(s)
                return unique_string(s)
            else:
                temp = j
                continue
        return s
assert(unique_string("abccba") == '')
assert(unique_string("foobar") == 'fbar')
assert(unique_string("abccbefggfe") == 'a')        
