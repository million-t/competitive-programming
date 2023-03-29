class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency = Counter(nums)
        frequency = [[count, num] for num, count in frequency.items()]
        length = len(frequency)
        
        def quickSort(pivot, right, arr):
            nonlocal length, k
            
            write = pivot + 1
            for read in range(pivot + 1, right):
                
                if arr[read] < arr[pivot]:
                    arr[read], arr[write] = arr[write], arr[read]
                    write += 1
            
            arr[pivot], arr[write - 1] = arr[write - 1], arr[pivot]
            
            
            if write - 1 == length - k:
                return [num for f, num in frequency[write - 1:]]
            
            if write - 1 > length - k:
                return quickSort(pivot, write - 1, arr)
            
            return quickSort(write, right, arr)
        
        
        
        return quickSort(0, length, frequency)
         