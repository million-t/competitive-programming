class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        
        processorTime.sort(reverse = True)
        tasks.sort()
        min_time = 0
        
        indx = 0
        for start in processorTime:
            
            for d in range(4):
                min_time = max(min_time, start + tasks[indx])
                indx += 1
        
        return min_time
        