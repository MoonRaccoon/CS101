def is_list(p):
    return isinstance(p, list)


def deep_reverse(l):
    f = []
    for e in l:
        f.insert(0, e)
        if is_list(e):
           f[0] = deep_reverse(e)
    return f