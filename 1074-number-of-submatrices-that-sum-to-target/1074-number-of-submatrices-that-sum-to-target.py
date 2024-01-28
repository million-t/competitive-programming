class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        
        rows, cols = len(matrix), len(matrix[0])
        
        for row in range(rows):
            for col in range(1, cols):
                matrix[row][col] += matrix[row][col - 1]
        
        ans = 0
        
        for right_col in range(cols):
            for left_col in range(right_col + 1):
                
                seen = defaultdict(int)
                seen[0] += 1
                pref = 0
                
                for row in range(rows):
                    cur_win = matrix[row][right_col]
                    if left_col:
                        cur_win -= matrix[row][left_col - 1]
                    
                    pref += cur_win
                    ans += seen[pref - target]
                    
                    seen[pref] += 1
                
        return ans
                