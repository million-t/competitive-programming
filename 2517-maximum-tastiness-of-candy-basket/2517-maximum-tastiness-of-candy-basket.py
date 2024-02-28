class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        
        
        def check(dif):
            
            count = 1
            last = 0
            for indx in range(1, len(price)):
                if price[indx] - price[last] >= dif:
                    last = indx
                    count += 1
            
            return count >= k
        
        left = 0
        right = price[-1] - price[0]
        
        while left <= right:
            mid = left + (right - left)//2

            if check(mid):
                left = mid + 1
            
            else:
                right = mid - 1
        
        
        return left - 1