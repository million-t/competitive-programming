class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        
        def inbounds(row, col):
            return 0 <= row < len(img2) and 0 <= col < len(img2)
        
        n = len(img1)
        ans = 0
        
        for dr in range(-n + 1, n):
            for dc in range(-n + 1, n):
                
                temp = 0
                for row in range(n):
                    for col in range(n):
                        
                        row2, col2 = row + dr, col + dc
                        
                        if inbounds(row2, col2) and img1[row][col] == img2[row2][col2] == 1:
                            temp += 1
                
                ans = max(ans, temp)
        
        return ans
                        
                        
        