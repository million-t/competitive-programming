class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        
        
        arr2.sort()
        
        @cache
        def dp(indx1, indx2, prev):
            
            if indx1 < 0:
                return 0
            
            ans = float('inf')
            

            if arr1[indx1] < prev:
                ans = dp(indx1 - 1, indx2, arr1[indx1])
            
            right = bisect_left(arr2, prev, 0, indx2 + 1)
            if right:
                ans = min(ans, dp(indx1 - 1, right - 1, arr2[right - 1]) + 1)
            
            return ans
        
        
        
        
        
        ans = dp(len(arr1) - 1, len(arr2) - 1, float('inf'))
        return ans if ans != float('inf') else -1
            
        