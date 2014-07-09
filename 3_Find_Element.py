def find_element(m, p):
    indexcount = 0
    for e in m:
        if e == p:
            return indexcount
        else:
            indexcount = indexcount + 1
    if e != p:
        return -1

print find_element(['alpha', 'beta'], 'gamma')
