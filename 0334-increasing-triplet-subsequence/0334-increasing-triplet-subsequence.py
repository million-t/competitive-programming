class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3: 
            return False
        
        ay = nums[0]
        jay = float('inf')
        
        for kay in nums:
            
            if kay > ay:
                if jay == float("inf"):
                    jay = kay
                
                elif kay > jay:
                    return True
                
                jay = kay
            
            else:
                ay = kay
                
        
        return False
            
                
            
        