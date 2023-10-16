class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        even = defaultdict(int)
        odd = defaultdict(int)
        
        
        for indx, num in enumerate(nums):
            
            if indx & 1:
                odd[num] += 1
            
            else:
                even[num] += 1
                          
        
        ans = float('inf')
        even_counts = sum(even.values())
        odd_counts = sum(odd.values())

        temp = sorted([(val, key) for key, val in odd.items()], reverse = True)
        _max = temp[0][0] if temp else 0
        sec_max = temp[1][0] if len(temp) > 1 else 0

        
        
        for num, count in even.items():
            
            ops = even_counts - count
            if temp and temp[0][1] == num:
                ops += odd_counts - sec_max
            
            else:
                ops += odd_counts - _max
                
            ans = min(ans, ops)
            
        
        return ans
        
        
                