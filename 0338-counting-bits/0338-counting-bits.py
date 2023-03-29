class Solution:
    def countBits(self, n: int) -> List[int]:
        
        ans = [0]
        
        sig_bit = 1
        
        for num in range(1, n + 1):
            
            if num & sig_bit<<1:
                sig_bit <<= 1
            
    
            ans.append(ans[num - sig_bit] + 1)
        
        return ans