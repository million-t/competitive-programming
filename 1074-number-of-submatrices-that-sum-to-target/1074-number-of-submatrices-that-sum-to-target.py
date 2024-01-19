class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        
        
        pref = [[0]*(len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        rows, cols = len(pref), len(pref[0])
        
        for row in range(1, rows):
            for col in range(1, cols):
                pref[row][col] += pref[row - 1][col] + pref[row][col - 1] - pref[row - 1][col - 1] + matrix[row - 1][col - 1]
                
        
        dp = defaultdict(lambda :defaultdict(int))
        ans = 0

        
        for col in range(1, cols):
            for prev in range(col - 1, -1, -1):
                dp[(prev, col)][0] = 1
        
        for row in range(1, rows):
            for col in range(1, cols):
                for prev in range(col - 1, -1, -1):
                    ans += dp[(prev, col)][pref[row][col] - pref[row][prev] - target]
                
                for prev in range(col - 1, -1, -1):
                    dp[(prev, col)][pref[row][col] - pref[row][prev]] += 1
                
                
        return ans        
        
        