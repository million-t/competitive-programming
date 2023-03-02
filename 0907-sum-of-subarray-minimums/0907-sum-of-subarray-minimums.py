class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        stack = []
        min_sum = 0
        
        increment = 0
        for num in arr:
             
            pop_count = 1
            
            while stack and stack[-1][0] >= num:
                larger, prev_pops =stack.pop() 
                
                increment -= prev_pops*larger
                pop_count += prev_pops
                
            stack.append([num, pop_count])
            
            increment += num*pop_count
            min_sum += increment
            

        return min_sum%(10**9 + 7)
           
        
            
        