class Solution:
    
    def mergeSorted(self, list1, list2):
        
        output = []
        first = second = 0 
        
        while first < len(list1) and second < len(list2):
            
            if list1[first] <= list2[second]:
                output.append(list1[first])
                first += 1
            
            else:
                output.append(list2[second])
                second += 1
                
        
        
        output.extend(list1[first:])
        output.extend(list2[second:])
        
        return output
    
    
    
    
    def sortArray(self, nums: List[int]) -> List[int]:
        
        if len(nums) <= 1:
            return nums
        
        mid = len(nums)//2
        
        return self.mergeSorted(self.sortArray(nums[:mid]), self.sortArray(nums[mid:]))
        
        