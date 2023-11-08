class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        
        dx = abs(fx - sx)
        dy = abs(fy - sy)
        
        if t == 1 and dx == dy == 0:
            return False
        
        return t >= max(dx, dy)
        