class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        stack = [intervals[0][0],intervals[0][1]]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= stack[-1]:
                if intervals[i][1] <= stack[-1]:
                    continue
                else:
                    stack.pop()
            else:
                stack.append(intervals[i][0])
            stack.append(intervals[i][1])
        merged = []
        for i in range(0,len(stack), 2):
            merged.append([stack[i], stack[i+1]])
        return merged

            
