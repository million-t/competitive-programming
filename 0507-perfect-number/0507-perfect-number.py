class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        divisor_sum = 1 if num!= 1 else 0
        
        for i in range(2, int(num**0.5) + 1):
            if not num%i:
                divisor_sum += i + num//i
        
        return divisor_sum == num
        