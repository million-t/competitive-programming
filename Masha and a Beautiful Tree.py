def helper(start, end):
    global impossible, swaps
 
    mid = start + (end - start)//2
 
    if mid == start or impossible:
        return permutation[mid], permutation[mid]
    
    
 
    min1, max1 = helper(start, mid)
    min2, max2 = helper(mid, end)
 
    if max1 <= min2:
        return min1, max2
 
    if min1 >= max2:
        swaps += 1
        return min2, max1
    
    
    impossible = True
    return 0, 0
 
tests = int(input())
 
for _ in range(tests):
    m = int(input())
    permutation = list(map(int, input().split()))
 
    swaps = 0
    impossible = False
 
    helper(0, len(permutation))
 
    if not impossible:
        print(swaps)
    
    else:
        print(-1)
