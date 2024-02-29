class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:    
        
        ans = []
        candidates.sort()
        
        def backtrack(start, path, path_sum):
            
            if path_sum == target:
                ans.append(path[:])
                return
            
            for indx in range(start, len(candidates)):
                if indx > start and candidates[indx] == candidates[indx - 1]:
                    continue
                
                if candidates[indx] + path_sum > target:
                    break
                
                path.append(candidates[indx])
                backtrack(indx + 1, path, path_sum + candidates[indx])
                path.pop()
        
        backtrack(0, [], 0)
        return ans