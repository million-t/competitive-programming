class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        n = len(nums)
        nums.insert(0, 1)
        nums.append(1)
        
        dp = [[0]*(n + 2) for _ in range(n + 2)]
        
        for indx in range(1, n + 1):
            dp[indx][indx] = nums[indx - 1]*nums[indx]*nums[indx + 1]
        
        
        
        for size in range(2, n + 1):
            for indx in range(1, n + 1):
                for start in range(max(0, indx - size + 1), min(indx + 1, n - size + 2)):
                    dp[start][start + size - 1] = max(dp[start][start + size - 1], nums[start - 1]*nums[indx]*nums[start + size] + dp[start][indx - 1] + dp[indx + 1][start + size - 1])
        
            
        return dp[1][n]
                    
                    
                    
                
        
        