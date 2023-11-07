class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        
        length = len(heights)
        ans = [0]*length
        stack = []
        
        for indx in range(length - 1, -1, -1):
            height = heights[indx]
            
            count = 0
            while stack and stack[-1] < height:
                stack.pop()
                count += 1
            
            ans[indx] = count + 1 if stack else count
            stack.append(height)
            
        
        return ans
        