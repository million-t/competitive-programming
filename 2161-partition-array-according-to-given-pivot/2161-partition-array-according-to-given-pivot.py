class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        nums_size = len(nums)
        
        less_ptr = 0
        equal_ptr = 0
        greater_ptr = 0
        
        for i in range(nums_size):
            if nums[i] < pivot:
                equal_ptr += 1
                greater_ptr += 1
            elif nums[i] == pivot:
                greater_ptr += 1
        
        partitioned = [0]*nums_size
        
        for num in nums:
            if num < pivot:
                partitioned[less_ptr] = num
                less_ptr += 1
                
            elif num == pivot:
                partitioned[equal_ptr] = num
                equal_ptr += 1
                
            else:
                partitioned[greater_ptr] = num
                greater_ptr += 1
        
        return partitioned
            