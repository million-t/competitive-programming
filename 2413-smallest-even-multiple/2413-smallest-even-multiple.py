class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        i = n
        while True:
            if not i%2:
                return i
            i += n
            
        