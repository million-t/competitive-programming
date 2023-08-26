class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        pairs.sort(key= lambda x: (x[1],x[0]))
        
        ans = 0
        prev_right = float('-inf')
        
        for left, right in pairs:
            if left > prev_right:
                prev_right = right
                ans += 1
        
        return ans
        
        