def find_element(p, m):
    if m in p:
        return p.index(m)
    else:
        return -1

print find_element([1, 2, 3], 3)

print find_element(['Snuggly', 'Wuggly', 'Teddy'], 'Wuggly')
