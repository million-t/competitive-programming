class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        count = Counter(nums)
        ans = []
        
        def backtrack(path):
            
            if len(path) == len(nums):
                ans.append(path[:])
                return
            
            for num in count:
                if count[num]:
                    count[num] -= 1
                    path.append(num)
                    backtrack(path)
                    path.pop()
                    count[num] += 1
        
        backtrack([])
        return ans
                    
        