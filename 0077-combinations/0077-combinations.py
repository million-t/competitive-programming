class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        combinations = []
        
        def backtrack(comb=[], index=1, count=0):
            nonlocal k, n
            
            if count == k:
                combinations.append(comb[:])
                return
            
            for num in range(index, n + 1):

                comb.append(num)

                backtrack(comb, num + 1, count + 1)

                comb.pop()
        
        backtrack()
        
        return combinations
            