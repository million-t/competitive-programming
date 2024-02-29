class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        
        ans = []
        candidates = list(range(1, 10))
        def backtrack(start, path, target):
            
            
            if not target:
                if len(path) == k:
                    ans.append(path[:])
                return 
            
            for indx in range(start, len(candidates)):    
                if target - candidates[indx] < 0:
                    break
                
                path.append(candidates[indx])
                backtrack(indx + 1, path, target - candidates[indx])
                path.pop()
            
        
        backtrack(0, [], n)
        return ans