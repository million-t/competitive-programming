m, n = list(map(int, input().split()))

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

ptr_1 = 0

smaller = []
for ptr_2 in range(n):
    while ptr_1 < m and arr1[ptr_1] < arr2[ptr_2]:
        ptr_1 += 1
    
    smaller.append(ptr_1)

print(*smaller)
