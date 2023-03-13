class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        max_length = len(nums)
        permutations = []
        
        def backtrack(items):
            nonlocal nums
            
            if  len(items) == max_length:
                permutations.append(items[:])
                return
            
            for val in nums:
                if val not in items:
                    items.append(val)
                    
                    backtrack(items)
                    
                    items.pop()
        
        backtrack([])
        return permutations        
                