from sortedcontainers import SortedList
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        
        
        
        def merge(left_sorted, right_sorted):
            
            strict_less = left = right = 0
            
            len_left = len(left_sorted)
            len_right = len(right_sorted)
            
            merged = []
            
            
            while left < len_left and right < len_right:
                if left_sorted[left][0] <= right_sorted[right][0]:
                    merged.append(left_sorted[left])
                    left += 1
                
                
                else:
                    
                    while strict_less < left and left_sorted[strict_less][0] < right_sorted[right][0]:
                        strict_less += 1
            
                        
                    right_sorted[right][1] += len_left - left    
                    right_sorted[right][2] += left - strict_less
                    
                    merged.append(right_sorted[right])
                    right += 1
            
        
            merged.extend(left_sorted[left:])
            
            
            while right < len_right:
            
                while strict_less < left and left_sorted[strict_less][0] < right_sorted[right][0]:
                    strict_less += 1

                right_sorted[right][1] += len_left - left    
                right_sorted[right][2] += left - strict_less

                merged.append(right_sorted[right])
                right += 1
            
            return merged
        
        def mergeSort(left, right, arr):
            
            if left >= right - 1:
                return [[arr[left], 0, 0, left]]
            
            mid = left + (right - left)//2
            
            left_half = mergeSort(left, mid, arr)
            right_half = mergeSort(mid, right, arr)
            
            return merge(left_half, right_half)
        
        
        sorted_instr = mergeSort(0, len(instructions), instructions)
        min_cost = 0
        
        
        
        
        for inst, shift, less, prev in sorted_instr:
            min_cost += min(shift, prev - (shift + less))
        
        
        return min_cost%(10**9 + 7)