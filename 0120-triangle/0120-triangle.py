class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        for ind in range(1, len(triangle)):
            
            prev_last = len(triangle[ind - 1]) - 1
            for j in range(len(triangle[ind])):
                triangle[ind][j] = triangle[ind][j] + min(triangle[ind - 1][max(j - 1, 0)], triangle[ind - 1][min(prev_last, j)])
        
        return min(triangle[-1])