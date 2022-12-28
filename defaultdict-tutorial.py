# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
size = list(map(int, input().split(' ')))
d = defaultdict(list)
for i in range(1, size[0] + 1):
    key = input()
    d[key].append(str(i))
for _ in range(size[1]):
    character = input()
    if character in d:
        print(' '.join(d[character]))
    else:
        print('-1')
