class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        ans = [height for height in heights]
        stack = []

        for indx in range(len(heights)):
            height = heights[indx]
            temp = 0
            saved_indx = indx
            
            while stack and stack[-1][0] >= height:
                prev_height, prev_indx = stack.pop()
                saved_indx = prev_indx
                temp = max(temp, height*(indx - prev_indx + 1))
                
            ans[indx] = max(ans[indx], temp)
            stack.append((height, saved_indx))
        
        
        stack = []
        for indx in range(len(heights) - 1, -1, -1):
            height = heights[indx]
            temp = 0
            saved_indx = indx
            
            while stack and stack[-1][0] >= height:
                prev_height, prev_indx = stack.pop()
                saved_indx = prev_indx
                temp = max(temp, height*(prev_indx - indx))
                
            ans[indx] += temp
            stack.append((height, saved_indx))
            
        
        return max(ans)
        