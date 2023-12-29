class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        temp = m
        m = n
        n = temp
        state = [[0]*m for i in range(n)]
        
        for i, j in guards:
            state[i][j] = 3
        
        for i, j in walls:
            state[i][j] = -1
            
        for row in range(n):
            for col in range(m):
                if state[row][col] == 3:
                    
                    for nr in range(row - 1, -1, -1):
                            
                        if state[nr][col] == -1 or state[nr][col] & 3 == 3 or state[nr][col] & 1 == 1:
                            break
                        
                        state[nr][col] |= 1
                    
                    for nc in range(col - 1, -1, -1):
                        if state[row][nc] == -1 or state[row][nc] & 3 == 3 or state[row][nc] & 2 == 2:
                            break
                        
                        state[row][nc] |= 2
                    
                    for nr in range(row + 1, n):
                        if state[nr][col] == -1 or state[nr][col] & 3 == 3 or state[nr][col] & 1 == 1:
                            break
                        
                        state[nr][col] |= 1
                    
                    for nc in range(col + 1, m):
                            
                        if state[row][nc] == -1 or state[row][nc] & 3 == 3 or state[row][nc] & 2 == 2:
                            break
                        
                        state[row][nc] |= 2
        
        ans = 0 
        
        for row in range(n):
            for col in range(m):
                if not state[row][col]:
                    ans += 1
        
        return ans
                        
                            