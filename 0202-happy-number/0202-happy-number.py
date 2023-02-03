class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = str(n)
            sqrSum = 0
            
            for dig in n:
                dig = int(dig)
                sqrSum += dig*dig
            
            n = sqrSum
        
        return n==1
            