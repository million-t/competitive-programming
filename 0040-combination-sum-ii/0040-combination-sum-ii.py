class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        candidates.sort()
        def backtrack(start, path, target):
            
            
            if not target:
                ans.append(path[:])
                return 
            
            for indx in range(start, len(candidates)):
                if indx > start and candidates[indx] == candidates[indx - 1]:
                    continue
                
                if target - candidates[indx] < 0:
                    break
                
                path.append(candidates[indx])
                backtrack(indx + 1, path, target - candidates[indx])
                path.pop()
            
        
        backtrack(0, [], target)
        return ans
                
        