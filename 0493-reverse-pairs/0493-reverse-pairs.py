class Solution:
    
    def __init__(self): 
        self.rev_pair_cnt = 0
    
    def merge(self, arr1, arr2):
        
    
        len_1, len_2 = len(arr1), len(arr2)    
        ptr_1 = ptr_2 = 0
        
        merged = []
        pos = 0
        count = 0
        while ptr_1 < len_1 and ptr_2 < len_2:
            
            if arr1[ptr_1] <= arr2[ptr_2]:
                
                while pos < len_2 and arr2[pos]*2 < arr1[ptr_1]:
                    pos += 1
                    
                count += pos
                
                merged.append(arr1[ptr_1])
                ptr_1 += 1
            
            else:
        
                merged.append(arr2[ptr_2])
                ptr_2 += 1
        
        while ptr_1 < len_1:
            while pos < len_2 and arr2[pos]*2 < arr1[ptr_1]:
                pos += 1
                    
            count += pos
            merged.append(arr1[ptr_1])
            ptr_1 += 1
            
        merged.extend(arr2[ptr_2:])
        
        self.rev_pair_cnt += count
        
        return merged
        
    
    def mergeSort(self, left, right, arr):
                
        if left >= right - 1:
            return [arr[left]]
        
        mid = left + (right - left)//2
        
        left_half = self.mergeSort(left, mid, arr)
        right_half = self.mergeSort(mid, right, arr)
        
        return self.merge(left_half, right_half)
        
    
    def reversePairs(self, nums: List[int]) -> int:
        
        self.mergeSort(0, len(nums), nums)
        
        
        return self.rev_pair_cnt
        