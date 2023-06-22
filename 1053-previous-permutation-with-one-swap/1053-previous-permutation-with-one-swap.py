class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        
        size = len(arr)
        stack = []
        
        for ind in range(size - 1, -1, -1):    
            num = arr[ind]
            last = None
            
            while stack and arr[stack[-1]] <= num:
                
                if arr[stack[-1]] == num:
                    stack.pop()
                
                else:
                    last = stack.pop()
            
            
            if last:
                arr[last], arr[ind] = arr[ind], arr[last]
                break
            
            stack.append(ind)
        
                
        return arr
        
        