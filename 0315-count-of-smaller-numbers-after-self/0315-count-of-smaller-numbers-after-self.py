class Solution:
     
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        
        res = [0]*len(nums)
        
        def merge(arr1, arr2):
            
            len_1, len_2 = len(arr1), len(arr2)    
            ptr_1 = ptr_2 = 0

            merged = []
            inc  = 0 
            while ptr_1 < len_1 and ptr_2 < len_2:

                if arr1[ptr_1][0] <= arr2[ptr_2][0]:

                    merged.append(arr1[ptr_1])
                    res[arr1[ptr_1][1]] += inc
                    ptr_1 += 1

                else:
                    inc += 1
                    merged.append(arr2[ptr_2])
                    ptr_2 += 1

            while ptr_1 < len_1:
                res[arr1[ptr_1][1]] += inc
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
        
        
        
        for ind in range(len(nums)):
            nums[ind] = (nums[ind], ind)
        
        mergeSort(0, len(nums), nums)
        
        return res