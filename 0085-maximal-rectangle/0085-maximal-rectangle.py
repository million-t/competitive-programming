class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        n, m = len(matrix), len(matrix[0])
        pref = [[0]*(m + 1) for _ in range(n)]
        
        
        for row in range(n):
            for col in range(m):
                pref[row][col] = pref[row][col - 1] + int(matrix[row][col])  
        
        ans = 0
        for left in range(m):
            for right in range(left, m):
                last = 0
                for row in range(n):
                    if pref[row][right] - pref[row][left - 1] != right - left + 1:
                        last = row + 1
                        continue
                    
                    ans = max(ans, (right - left + 1)*(row - last + 1))
        
        return ans
        
        