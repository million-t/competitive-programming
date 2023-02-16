n = int(input())

arr = list(map(int, input().split()))

sortable = False
for i in range(1, n):
    if (arr[i] + arr[i-1])%2:
        sortable = True
        break

if sortable:
    arr.sort()
print(*arr)
