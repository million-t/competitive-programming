class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        
        last_sign = '='
        max_turb = 1 
        
        left = 0
        for right in range(1, len(arr)):
            
            if arr[right - 1] < arr[right]:
                
                if last_sign != '>':
                    left = right - 1
                
                last_sign = '<'

            
            
            elif arr[right - 1] > arr[right]:
                
                if last_sign != '<':
                    left = right - 1
                    
                last_sign = '>'
                
                
            
            elif arr[right - 1] == arr[right]:
                
                left = right
                last_sign = '='
            
            
            max_turb = max(max_turb, right - left + 1)
            
        
        return max_turb
            
            
                
                