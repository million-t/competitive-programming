from math import factorial

n = int(input())

def combination(n, r):

    ans = 1
    smaller = max(r, n - r)
    larger = min(r, n - r)
    while n > larger:
        ans *= n
        n -= 1
    
    return ans//factorial(smaller)



ans = combination(n, 5) + combination(n, 6) + combination(n, 7)
print(ans)