def key_strokes(s):
    if len(s) == 0:
        return ""
    else:
        for i,j in enumerate(s):
            if j == '#':
                return key_strokes(s[:i-1] + s[i+1:])
        return s
assert(key_strokes("ABC#") == key_strokes("CD##AB"))
assert(key_strokes("como#pur#ter") == key_strokes("computer"))
assert(key_strokes("cof#dim#ng") == key_strokes("code"))           
