from collections import Counter

m, n = list(map(int, input().split()))

mat = []
for _ in range(m):
    mat.append(input())

row_count_map = {}
col_count_map = {}
for i, row in enumerate(mat):
    row_count_map[i] = Counter(row)

for j in range(n):
    count = {}
    i = 0
    for i in range(m):
        cur = mat[i][j]
        count[cur] = count.get(cur, 0) + 1
    col_count_map[j] = count

decoded = []

for i in range(m):
    for j in range(n):
        cur_char = mat[i][j]
        if col_count_map[j][cur_char] == row_count_map[i][cur_char] == 1:
            decoded.append(cur_char)
print(''.join(decoded)) 
