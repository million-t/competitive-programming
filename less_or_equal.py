n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))

nums.sort()
if 0 < k < n and nums[k] == nums[k-1]:
    print(-1)
elif k == 0:
    if nums[0] > 1:
        print(1)
    else:
        print(-1)
else:
    print(nums[k - 1])
