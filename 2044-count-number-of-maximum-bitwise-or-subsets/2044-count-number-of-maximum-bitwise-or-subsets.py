class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        
        def find_or(a, b):
            return a | b
        
        max_or = reduce(find_or, nums)
        count = 0
        
        
        def backtrack(start, cur_or, max_or):
            nonlocal count
            
            if start and cur_or == max_or:
                count += 1
                
            
            for index in range(start, len(nums)):
                
                backtrack(index + 1, cur_or | nums[index], max_or)

        
        backtrack(0, 0, max_or)
        
        return count
            