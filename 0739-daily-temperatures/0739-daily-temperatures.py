class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        ans = [0]*len(temperatures)
        stack = []
        
        for indx, num in enumerate(temperatures):
            
            while stack and temperatures[stack[-1]] < num:
                temp = stack.pop()
                ans[temp] = indx - temp
            
            stack.append(indx)
        
        return ans
            
        