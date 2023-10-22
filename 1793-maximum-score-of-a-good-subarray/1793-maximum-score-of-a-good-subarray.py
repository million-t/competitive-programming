class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        
        
        stack = []
        
        for indx in range(k + 1):
            num = nums[indx]
            start = indx
            
            while stack and stack[-1][0] >= num:
                prev, start = stack.pop()
            
            stack.append((num, start))
        
        rev_stack = []
        for indx in range(len(nums) - 1, k - 1, -1):
            num = nums[indx]
            start = indx
            
            while rev_stack and rev_stack[-1][0] >= num:
                prev, start = rev_stack.pop()
            
            rev_stack.append((num, start))
        
        
        def finish(template, space):
            ans = 0
            
            for _min, i in template:
                pos = bisect_left(space, (_min, -1))
                lim, j = space[pos]
                ans = max(ans, _min*(max(i, j) - min(i, j) + 1))
            
            return ans
        
        return max(finish(stack, rev_stack), finish(rev_stack, stack))
        
            
        