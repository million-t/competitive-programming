class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        
        dp1 = [0]*len(nums1)
        dp2 = [0]*len(nums2)
        mod = 10**9 + 7
        
        i1 = 0
        i2 = 0
        
        while i1 < len(nums1) or i2 < len(nums2):
            if i1 < len(nums1) and i2 < len(nums2):
                if nums1[i1] < nums2[i2]:
                    dp1[i1] += dp1[i1 - 1] + nums1[i1]
                    i1 += 1
                
                elif nums1[i1] > nums2[i2]:
                    dp2[i2] += dp2[i2 - 1] + nums2[i2]
                    i2 += 1
                
                else:
                    dp1[i1] += max(dp2[i2 - 1], dp1[i1 - 1]) + nums2[i2]
                    dp2[i2] += max(dp2[i2 - 1], dp1[i1 - 1]) + nums2[i2]
                    
                    i1 += 1
                    i2 += 1
                    
            elif i1 < len(nums1):
                dp1[i1] += dp1[i1 - 1] + nums1[i1]
                i1 += 1
            
            else:
                dp2[i2] += dp2[i2 - 1] + nums2[i2]
                i2 += 1
                
        ans = max(dp1[-1], dp2[-1]) % mod
        return ans
        