class Solution:
    def subtractProductAndSum(self, n: int) -> int:
                
        _sum = 0
        product = 1
        
        while n:
            dig = n%10 
            _sum += dig
            product *= dig
            n //= 10
            
        return product - _sum 