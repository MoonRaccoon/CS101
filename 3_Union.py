def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)

a = [1, 2, 3]
b = [2, 4, 6]

union(a, b)

print a
