class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        length = len(nums)
        
        
        
        def quickSort(pivot, right, arr, target):
            
            if right <= pivot: return arr[pivot]

            write = pivot + 1

            for read in range(pivot + 1, right + 1):
                if arr[read] <= arr[pivot]:
                    arr[write], arr[read] = arr[read], arr[write]
                    write += 1
            
            
            arr[pivot], arr[write - 1] = arr[write - 1], arr[pivot]
            
            if write - 1 == target:
                return arr[target]
            
            elif target < write - 1:
                return quickSort(pivot, write - 2, arr, target)
            
            return quickSort(write, right, arr, target)
        
        
        return quickSort(0, length - 1, nums, length - k)