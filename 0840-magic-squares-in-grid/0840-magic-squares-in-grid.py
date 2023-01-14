class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def helper(r, c):
            distinct = set()
            sums = set()
            for col in range(c, c + 3):
                colSum = 0
                for row in range(r, r + 3):
                    if 0 < grid[row][col] <= 9:
                        distinct.add(grid[row][col])
                    colSum += grid[row][col]
                sums.add(colSum)
            diag1, diag2 = 0, 0
            for row in range(r, r + 3):
                rowSum = 0
                for col in range(c, c + 3):
                    rowSum += grid[row][col]
                    if (row - r) - (col - c) == 0:
                        diag1 += grid[row][col]
                    if (row - r) + (col - c) == 2:
                        diag2 += grid[row][col]
                sums.add(rowSum)
            sums.add(diag1)
            sums.add(diag2)
            return len(distinct) == 9 and len(sums) == 1
        
        magic_count = 0
        for row in range(len(grid) - 2):
            for col in range(len(grid[0]) - 2):
                if helper(row,col):
                    magic_count += 1
        return magic_count
            