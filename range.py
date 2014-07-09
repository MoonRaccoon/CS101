def bigger(a, b):
    if a > b:
        return a
    else:
        return b

def smaller(a, b):
    if a < b:
        return a
    else:
        return b

def biggest(a, b, c):
    return bigger(a, bigger(b, c))

def smallest(a, b, c):
    if  biggest(a, b, c) == a:
        med = smaller(b, c)
        return med
    if  biggest(a, b, c) == b:
        med = smaller(a,c)
        return med
    if  biggest(a, b, c) == c:
        med = smaller(a,b)
        return med


def set_range(a, b, c):
    maximum = biggest(a, b, c)
    minimum = smallest(a, b ,c)
    return maximum - minimum
