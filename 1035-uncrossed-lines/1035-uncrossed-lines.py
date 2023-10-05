class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        
        
        @cache
        def dp(indx1, indx2):
            
            if indx1 < 0 or indx2 < 0:
                return 0
            
            
            if nums1[indx1] == nums2[indx2]:
                return dp(indx1 - 1, indx2 - 1) + 1
            
            return max(dp(indx1 - 1, indx2), dp(indx1, indx2 - 1))
            
            
        return dp(len(nums1) - 1, len(nums2) - 1)