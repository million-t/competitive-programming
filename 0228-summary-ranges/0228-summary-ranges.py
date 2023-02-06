class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        output = []
        
        index = 0
        size = len(nums)
        while index < size:
            
            rng = [str(nums[index])]
            while index<size - 1 and nums[index + 1] == nums[index] + 1:
                index += 1
            
            if rng[-1] != str(nums[index]):
                rng.append('->')
                rng.append(str(nums[index]))
                
            output.append(''.join(rng))
            index+=1
        
        return output