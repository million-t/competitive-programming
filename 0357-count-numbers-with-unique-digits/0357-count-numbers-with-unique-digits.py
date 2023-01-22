class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        unique = 1
        
        for i in range(1, n + 1):
            unique += 9*factorial(9)//factorial(9-(i-1))
        
        return unique