class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        
        diff_arr = [nums1[ind] - nums2[ind] for ind in range(len(nums2))]
        pairs = 0
        
        def merge(arr1, arr2):
            nonlocal pairs, diff
            
            len_1, len_2 = len(arr1), len(arr2)    
            ptr_1 = ptr_2 = 0

            merged = []
            
            ind = 0
            
            while ptr_1 < len_1 and ptr_2 < len_2:
                
                if arr1[ptr_1] < arr2[ptr_2]:
                    
                    while ind < len_2 and arr1[ptr_1] > arr2[ind] + diff:
                        ind += 1
                    
                    pairs += len_2 - ind
                    
                    merged.append(arr1[ptr_1])
                    ptr_1 += 1

                else:
                    merged.append(arr2[ptr_2])
                    ptr_2 += 1

            while ptr_1 < len_1:
                
                while ind < len_2 and arr1[ptr_1] > arr2[ind] + diff:
                    ind += 1
                    
                pairs += len_2 - ind
        
                merged.append(arr1[ptr_1])
                ptr_1 += 1

            merged.extend(arr2[ptr_2:])
            
            return merged


        
        def mergeSort(left, right, arr):

            if left >= right - 1:
                return [arr[left]]

            mid = left + (right - left)//2

            left_half = mergeSort(left, mid, arr)
            right_half = mergeSort(mid, right, arr)

            return merge(left_half, right_half)
        
        mergeSort(0, len(diff_arr), diff_arr)
        
        return pairs
        
