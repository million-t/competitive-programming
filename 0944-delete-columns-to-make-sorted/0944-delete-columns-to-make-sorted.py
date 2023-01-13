class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        deleted = 0
        
        for col in range(len(strs[0])):
            prev = strs[0][col]
            for row in range(len(strs)):
                if strs[row][col] < prev:
                    deleted += 1
                    break
                prev = strs[row][col]
        
        return deleted