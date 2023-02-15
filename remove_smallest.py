t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()

    broken = False
    for i in range(1, len(arr)):
    
        if arr[i] - arr[i-1] > 1:
            print("NO")
            broken = True
            break
    
    if not broken:
        print("YES")
    
    
