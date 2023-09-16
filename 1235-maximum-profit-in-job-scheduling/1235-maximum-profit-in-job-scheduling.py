class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        temp = [triplet for triplet in zip(endTime, startTime, profit)]
        
        length = len(startTime)
        dp = [0]*length
        
        temp.sort()
        for ind, (end, start, prof) in enumerate(temp):
            dp[ind] = max(dp[ind - 1], dp[bisect_right(temp, (start, start)) - 1] + prof)
        
        return dp[-1]
        
            
        