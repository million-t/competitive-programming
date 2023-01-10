class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        prefix_sums = []
        prefix = 0
        for num in arr:
            prefix_sums.append(prefix)
            prefix += num
        
        tot_sub_arr_sum = 0
        for right in range(len(arr)):
            
            left = right
            while left >= 0:
                tot_sub_arr_sum += prefix_sums[right] + arr[right] - prefix_sums[left]
                left -= 2
        
        return tot_sub_arr_sum