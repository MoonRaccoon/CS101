def stirling(n, k):
    if k == 1 or n == k:
        return 1
    if k > n:
        return 0
    return k * stirling(n-1, k) + stirling(n-1, k-1)
    

def bell(n):
    k = 1
    result = 0
    while k <= n:
        result += stirling(n, k)
        k += 1
    return result
        
    