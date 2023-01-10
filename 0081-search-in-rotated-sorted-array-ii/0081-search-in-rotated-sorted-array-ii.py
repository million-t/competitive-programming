class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def bin_search(arr, target):
            start = 0
            end = len(arr) - 1
        
            while start <= end:
                mid = (start + end)//2
            
                if target < arr[mid]:
                    end = mid - 1
            
                elif target > arr[mid]:
                    start = mid + 1
            
                elif target == arr[mid]:
                    return True
                
            return False
        

        k = 0
        while k < len(nums) and nums[k] >= nums[k-1]:
            k += 1
        print(k)
        return bin_search(nums[:k], target) or bin_search(nums[k:], target)
            
        
        
        
        