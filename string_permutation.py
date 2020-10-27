def permute (s):
    out = []
    
    if len(s) == 1:
        out = [s]
    else:
        for i, let in enumerate(s):
                for perm in permute( s[:i] + s[i+1:]):
                    print(perm)
                    out += [let+perm]
                    print(out)
    return out
