class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        @cache
        def dp(indx1, indx2):
            
            
            if indx1 >= len(nums1) or indx2 >= len(nums2):
                return float('-inf')
            
            return max(
                dp(indx1 + 1, indx2),
                dp(indx1, indx2 + 1),
                max(dp(indx1 + 1, indx2 + 1) + nums1[indx1]*nums2[indx2], nums1[indx1]*nums2[indx2])
                )
        
        return dp(0, 0)