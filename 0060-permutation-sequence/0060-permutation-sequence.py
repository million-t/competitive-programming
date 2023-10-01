class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        steps = 0
        ans = []
        
        def backtrack(perm, visited):
            nonlocal ans, steps
            
            if len(ans) > 0:
                return
            
            if len(perm) == n:
                steps += 1
                if steps == k:
                    ans = perm[:]    
                    
                return 
            
            for num in range(1, n + 1):
                if num not in visited:
                    perm.append(num)
                    visited.add(num)
                    backtrack(perm, visited)
                    perm.pop()
                    visited.remove(num)
            
        
        backtrack([], set())
        return ''.join(map(str, ans))