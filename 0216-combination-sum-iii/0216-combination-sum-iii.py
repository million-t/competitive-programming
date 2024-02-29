class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        ans = []
        candidates = list(range(1, 10))
        
        def backtrack(start, path, path_sum):
            
            if path_sum == n:
                if len(path) == k:
                    ans.append(path[:])
                return
            
            if len(path) > k:
                return
            
            for indx in range(start, len(candidates)):
                if candidates[indx] + path_sum > n:
                    break
                
                path.append(candidates[indx])
                backtrack(indx + 1, path, path_sum + candidates[indx])
                path.pop()
        
        backtrack(0, [], 0)
        return ans