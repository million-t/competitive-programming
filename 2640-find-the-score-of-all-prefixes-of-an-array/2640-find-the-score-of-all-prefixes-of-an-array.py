class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        
        
        cur_max = 0
        conv_sum = 0
        ans = []
        
        for num in nums:
            cur_max = max(cur_max, num)
            cur_conv = cur_max + num
            conv_sum += cur_conv 
            ans.append(conv_sum)
        
        return ans
            
        