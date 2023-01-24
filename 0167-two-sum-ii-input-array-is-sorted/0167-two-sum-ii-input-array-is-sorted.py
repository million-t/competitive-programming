class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        
        while left < right:
            curSum = numbers[left] + numbers[right]
            
            if curSum < target:
                left+=1
                
            elif curSum > target:
                right-=1
                
            else:
                return [left + 1, right + 1]
        
            
