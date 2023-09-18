class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        rows, cols = len(dungeon), len(dungeon[0])
        
        for row in range(rows - 2, -1, -1):
            dungeon[row][-1] += min(0, dungeon[row + 1][-1])
        
        for col in range(cols - 2, -1, -1):
            dungeon[-1][col] += min(0, dungeon[-1][col + 1])
        
        for row in range(rows - 2, -1, -1):
            for col in range(cols - 2, -1, -1):
                dungeon[row][col] += max(min(dungeon[row + 1][col], 0), min(dungeon[row][col + 1], 0))
                
        
        
        return -dungeon[0][0] + 1 if dungeon[0][0] <= 0 else 1 
        