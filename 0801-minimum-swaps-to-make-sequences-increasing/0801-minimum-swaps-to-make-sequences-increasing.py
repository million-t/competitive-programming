class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        
        
        @cache
        def dp(indx, prev1, prev2):
            
            if indx < 0:
                return 0
            
            temp = float('inf')
            if nums1[indx] < prev1 and nums2[indx] < prev2:
                temp = dp(indx - 1, nums1[indx], nums2[indx])
            
            if nums2[indx] < prev1 and nums1[indx] < prev2:
                temp = min(temp, dp(indx - 1, nums2[indx], nums1[indx]) + 1)
            
            return temp
        
        
        
        return dp(len(nums1) - 1, float('inf'), float('inf'))
            
        