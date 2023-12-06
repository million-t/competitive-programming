class Solution:
    def totalMoney(self, n: int) -> int:
        
        
        dep = 0
        last_mon = 0
        prev = 0
        
        for num in range(n):
            if not num % 7:
                prev = last_mon
                last_mon += 1
            
            prev += 1
            dep += prev
        
        return dep
            
                