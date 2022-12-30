class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        for row in range(m):
            temp = 0
            for col in range(n):
                val = grid[row][col]
                if row == 0 and col == 0:
                    grid[row][col] = [val, val , val]
                elif row == 0:
                    grid[row][col] = [val, val + grid[row][col - 1][1], val]
                elif col == 0:
                    grid[row][col] = [val, val , val + grid[row - 1][col][2]]
                else:
                    grid[row][col] = [val, val + grid[row][col - 1][1], val + grid[row - 1][col][2]]
        ans = []
        for i in range(m):
            newRow = []
            onesRow = grid[i][-1][1]
            zerosRow = n - onesRow
            for j in range(n):
                onesCol = grid[-1][j][2]
                zerosCol= m - onesCol
                newRow.append(onesRow + onesCol - (zerosRow + zerosCol))
            ans.append(newRow)
        return ans


