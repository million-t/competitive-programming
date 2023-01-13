

t = int(input())
for _ in range(t):
    m, n = list(map(int, input().split()))
    mat = []
    maxSum = 0
    for _ in range(m):
        mat.append(list(map(int, input().split())))
    
    first_diag = {}
    second_diag = {}

    for row in range(m):
        for col in range(n):
            first_diag[row+col] = first_diag.get(row+col, 0) + mat[row][col]
            second_diag[row-col] = second_diag.get(row-col, 0) + mat[row][col]
    maxx = 0
    for row in range(m):
        for col in range(n):
            maxx = max(maxx, first_diag[row + col] + second_diag[row - col] - mat[row][col])
    print(maxx)
