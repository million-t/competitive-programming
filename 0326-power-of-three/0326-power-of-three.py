class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        
        while n >= 1:
            
            if n == 1:
                return True
            
            n /= 3
            
        return False
#         if n == 1:
#             return True
        
#         elif n < 1 or n%3:
#             return False
        
#         return self.isPowerOfThree(n/3)
        