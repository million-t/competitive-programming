class Solution:
    def numberOfMatches(self, n: int) -> int:
        
        matches = 0
        while n > 1:
            temp = (n%2) + ((n - (n%2))//2) 
            matches += temp - n%2
            n = temp
        
        return matches
        