class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        
        ans = 0
        while target > 1:
            if not maxDoubles:
                ans += target - 1
                break
            
            if maxDoubles and not target & 1:
                target //= 2
                ans += 1
                maxDoubles -= 1
                
            else:
                target -= 1
                ans += 1
        
        return ans
                
        