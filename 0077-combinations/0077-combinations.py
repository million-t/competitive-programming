class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        nums = list(range(1, n + 1))
        ans = []
        
        def backtrack(indx, comb):
            
            if len(comb) == k:
                ans.append(comb[:])
                return
            
            if indx >= n:
                return 
            
            # insert
            comb.append(nums[indx])
            backtrack(indx + 1, comb)
            comb.pop()
            
            # not insert
            backtrack(indx + 1, comb)
            
        
        backtrack(0, [])
        return ans
            