class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        
        cur_num = 1
        ans = []
        
        for num in target:
            while num > cur_num:
                ans.append('Push')
                ans.append('Pop')
                cur_num += 1
            
            ans.append('Push')    
            cur_num += 1
            
        return ans