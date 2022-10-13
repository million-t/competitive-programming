class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans  = [0]*len(temperatures)
        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                poppedIndex = stack.pop()[0]
                ans[poppedIndex] = index - poppedIndex
            stack.append([index,temp])
        return ans
