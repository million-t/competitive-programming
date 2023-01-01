from collections import defaultdict
def is_valid(arr, s):
    pair = defaultdict(set)

    for indx, val in enumerate(arr):
        pair[val].add(s[indx])
        if len(pair[val]) > 1:
            return False
    return True

num_tests = int(input())
for _ in range(num_tests):
    n = int(input())
    arr = input().split(' ')
    s = input()

    result = is_valid(arr, s)
    if result:
        print('YES')
    else:
        print('NO')


