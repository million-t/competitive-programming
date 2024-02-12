class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        
        ans = [1]*n
        k -= n
        
        for indx in range(n - 1, -1, -1):
            plus = min(25, k)
            ans[indx] += plus
            k -= plus
            
            if not k:
                break
        
        for indx in range(n):
            ans[indx] = chr(ord('a') + ans[indx] - 1)
        
        return "".join(ans)
        
        