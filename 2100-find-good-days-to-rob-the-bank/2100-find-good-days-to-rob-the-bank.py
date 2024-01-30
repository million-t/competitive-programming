class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        
        inc = [0]*len(security)
        dec = [0]*len(security)
        
        for indx in range(1, len(security)):
            if security[indx] <= security[indx - 1]:
                dec[indx] += dec[indx - 1] + 1
            
            if security[~indx] <= security[~(indx - 1)]:
                inc[~indx] += inc[~(indx - 1)] + 1
        
        ans = []
        for indx in range(time, len(security) - time):
            if dec[indx] - dec[indx - time] == time and inc[indx] - inc[indx + time] == time:
                ans.append(indx)
        
        
        return ans
        