class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums_size = len(nums)
        
        rearranged_nums = [0]*nums_size
        # rearranged must start from +ve from the problem description so...
        positive_ptr = 0 
        negative_ptr = 1

        for num in nums:
            if num > 0:
                rearranged_nums[positive_ptr] = num
                positive_ptr += 2 # incremented by two because we must alternate b/n +ve and -ve
            else:
                rearranged_nums[negative_ptr] = num
                negative_ptr += 2
        
        return rearranged_nums