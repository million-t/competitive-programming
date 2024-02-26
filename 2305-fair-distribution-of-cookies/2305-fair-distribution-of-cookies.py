class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        ans = float('inf')
        
        def backtrack(indx, dist, max_so_far):
            nonlocal ans
            
            if indx >= len(cookies):
                ans = min(ans, max_so_far)
                return
            
            if max_so_far >= ans:
                return
            
            for person in range(k):
                dist[person] += cookies[indx]
                backtrack(indx + 1, dist, max(max_so_far, dist[person]))
                dist[person] -= cookies[indx]
        
        backtrack(0, [0]*k, 0)
        
        return ans