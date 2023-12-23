class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        
        mult = 1
        temp = Counter(str(n))
        
        while mult <= 1_000_000_000:
            if Counter(str(mult)) == temp:
                return True
            
            mult *= 2
            
        
        return False
            
        