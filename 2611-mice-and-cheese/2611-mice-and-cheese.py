class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        
        
        temp = sorted([(r1 - r2, r1, r2) for r1, r2 in zip(reward1, reward2)], reverse=True)
        
        ans = 0
        for indx in range(len(temp)):
            dif, r1, r2 = temp[indx]
            if indx < k:
                ans += r1
            
            else:
                ans += r2
        
        return ans
        
        