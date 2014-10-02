def countdown(p):
    nums = []
    i = 0
    while i < p:
        nums.append(p - i)
        i += 1
    return nums

def triangular(n):
    return sum(countdown(n))