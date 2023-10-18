class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        
        def count(num):
            tot = 0
            delta = 1
            
            while num <= n:
                tot += min(n - (num - 1), delta)
                num *= 10
                delta *= 10
            
            return tot
        
        
        num = 1
        cur_indx = 1
        
        while cur_indx < k:
            lower = count(num)
            if cur_indx + lower > k:
                num *= 10
                cur_indx += 1
            
            else:
                num += 1
                cur_indx += lower
                        
        return num
        
        
        