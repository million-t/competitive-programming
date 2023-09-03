class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        def backtrack(start_ind, _sum, path):
            if _sum == target:
                ans.append(path.copy())
                return
            
            for ind in range(start_ind, len(candidates)):
                num = candidates[ind]
                temp = _sum + num
                if temp > target:
                    continue
                
                path.append(num)
                backtrack(ind, temp, path)
                path.pop()
        
        backtrack(0, 0, [])
        return ans