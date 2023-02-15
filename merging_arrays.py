m, n = list(map(int, input().split()))

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

ans = []

ptr1, ptr2 = 0, 0

while ptr1<m and ptr2<n:

    if arr1[ptr1] < arr2[ptr2]:
        ans.append(arr1[ptr1])
        ptr1 += 1

    else:
        ans.append(arr2[ptr2])
        ptr2 += 1

ans.extend(arr1[ptr1:])
ans.extend(arr2[ptr2:])

print(*ans)
