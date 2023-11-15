class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        
        arr.sort()
        arr[0] = 1
        
        for indx in range(1, len(arr)):
            arr[indx] = min(arr[indx], arr[indx - 1] + 1)
        
        return arr[-1]
                
            
        