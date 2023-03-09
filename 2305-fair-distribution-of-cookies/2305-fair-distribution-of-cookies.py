class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        min_dist = float('inf')
        distribution = [0]*k
        
        def backtrack(index):
            nonlocal min_dist
            
            if index >= len(cookies):
                min_dist = min(min_dist, max(distribution))
                return
            
            for i in range(k):
                distribution[i] += cookies[index]
                
                if distribution[i] >= min_dist:
                    distribution[i] -= cookies[index]
                    continue
                
                backtrack(index + 1)
                
                distribution[i] -= cookies[index]
            
        
        backtrack(0)
        
        return min_dist