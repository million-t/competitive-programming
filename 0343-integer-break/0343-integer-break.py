class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2: return 1
        
        ans = 0
        for k in range(2, n):
            quot = n//k
            mod = n%k

            temp = [quot]*k
            i = 0
            while mod:
                temp[i] += 1
                mod -= 1
                i += 1

            prod = 1
            for num in temp:
                prod *= num
            
            ans = max(prod, ans)
            
        return ans
        
        