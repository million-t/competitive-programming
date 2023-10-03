class Solution:
    def maxScore(self, nums: List[int]) -> int:
        
        length = len(nums)
        temp = []
        
        for indx in range(length):
            for sec_indx in range(indx + 1, length):
                temp.append((indx, sec_indx, math.gcd(nums[indx], nums[sec_indx])))
        
        
        @cache
        def dp(i, mask):
            
            ans = 0
            for indx, sec_indx, gcd in temp:
                bit_1 = 1 << indx
                bit_2 = 1 << sec_indx
                
                if not ((mask & bit_1) or (mask & bit_2)):
                    new_mask = ((mask|bit_1)|bit_2)
                    ans = max(ans, i*gcd + dp(i + 1, new_mask))
                    
            return ans
        
        return dp(1, 0)
            
            
        