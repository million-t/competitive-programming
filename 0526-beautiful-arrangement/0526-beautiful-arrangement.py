class Solution:
    def countArrangement(self, n: int) -> int:
        
        beautiful_arrangement = 0 
        
        def backtrack(start, index, visited):
            nonlocal beautiful_arrangement
            
            if index > n:
                beautiful_arrangement += 1
                return
            
            for num in range(1, n + 1):
                
                check_bit = 1 << num - 1
                
                if (check_bit & visited) or (num%index and index%num):
                    continue
                    
                visited ^= check_bit
                backtrack(num + 1, index + 1, visited)
                visited ^= check_bit
        
        backtrack(1, 1, 0)
        
        return beautiful_arrangement