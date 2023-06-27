class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        processes = sorted([(arrival, length, ind) for ind, (arrival, length) in enumerate(tasks)])
        ind = 1
        heap = [(processes[0][1], processes[0][2], processes[0][0])]
        ans = []
        cur_time = processes[0][0]
        
        while heap:
            length, task_ind, arrival = heappop(heap)
            ans.append(task_ind)
            cur_time += length
            
            while ind < len(processes) and processes[ind][0] <= cur_time:
                start, time, _ind = processes[ind]
                heappush(heap, (time, _ind, start))
                ind += 1
            
            if ind < len(processes) and not heap:
                start, time, _ind = processes[ind]
                heappush(heap, (time, _ind, start))
                cur_time = start
                ind += 1
        
        return ans
                                           
                                          