class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hashmap = {}
        
        for i, num in enumerate(nums2):
            
            while stack and nums2[stack[-1]] < num:    
                hashmap[nums2[stack.pop()]] = num
            
            stack.append(i)
        
        greatest = []
        for num in nums1:
            greatest.append(hashmap.get(num, -1))
        
        return greatest