class Solution:
    @cache
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        
        return 1 + min(self.integerReplacement(n + 1), self.integerReplacement(n - 1)) if n & 1 else 1 + self.integerReplacement(n//2)
        