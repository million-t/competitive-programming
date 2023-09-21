class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        def search(shorter_arr, longer_arr):
            
            shorter_len = len(shorter_arr)
            longer_len = len(longer_arr)
            
            start = 0
            end = shorter_len
            comb_mid = (shorter_len + longer_len + 1)//2
            has_even_length = (shorter_len + longer_len) % 2 == 0
            
            while start <= end:
                shorter_mid = start + (end - start)//2
                longer_mid = comb_mid - shorter_mid
                
                
                min_from_shorter = shorter_arr[shorter_mid - 1] if shorter_mid > 0 else float('-inf') 
                max_from_shorter = shorter_arr[shorter_mid] if shorter_mid < shorter_len else float('inf')
                
                
                min_from_longer = longer_arr[longer_mid - 1] if longer_mid > 0 else float('-inf')
                max_from_longer = longer_arr[longer_mid] if longer_mid < longer_len else float('inf')
                
                if min_from_shorter <= max_from_longer and min_from_longer <= max_from_shorter:
                    if has_even_length:
                        return (max(min_from_longer, min_from_shorter) + min(max_from_longer, max_from_shorter))/2
                    
                    return max(min_from_longer, min_from_shorter)
                
                elif min_from_shorter < min_from_longer:
                    start = shorter_mid + 1
                
                else:
                    end = shorter_mid - 1
            
            
        if len(nums1) <= len(nums2):
            return search(nums1, nums2)
        
        return search(nums2, nums1)
                