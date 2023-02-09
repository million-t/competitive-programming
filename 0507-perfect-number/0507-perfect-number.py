class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        divisors = [1] if num!= 1 else []
        
        for i in range(2, int(num**0.5) + 1):
            if not num%i:
                divisors.extend([i, num//i])
        
        return sum(divisors) == num
        