class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        
        def gcd(a, b):
            if not b:
                return a
            
            return gcd(b, a%b)

        count = 0
        for cur_start in range(len(nums)):
            
            cur_gcd = 0
            for index in range(cur_start, len(nums)):
                cur_gcd = gcd(nums[index], cur_gcd)
                
                if cur_gcd == k:
                    count += 1
                
                elif cur_gcd < k:
                    break
        
        return count
        