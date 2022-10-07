from math import ceil

n, m, a = map(int, input().split(' '))
output = ceil(m/a)*ceil(n/a)
print(output)

