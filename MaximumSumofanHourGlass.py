class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        for row in range(len(grid)):
            curSum = 0
            for col, val in enumerate(grid[row]):
                grid[row][col] = [val, curSum]
                curSum+=val
        maxSum = 0
        for i in range(2, len(grid)):
            for j in range(2,len(grid[0])):
                temp = sum(grid[i][j]) + sum(grid[i-2][j]) + grid[i-1][j-1][0] - grid[i][j-2][1] - grid[i-2][j-2][1]
                maxSum = max(maxSum, temp) 

        return maxSum
