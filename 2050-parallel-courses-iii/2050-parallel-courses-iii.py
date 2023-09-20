class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        
        graph = [[] for _ in range(n)]
        indegree = defaultdict(int)
        
        for prev, _next in relations:
            graph[prev - 1].append(_next - 1)
            indegree[_next - 1] += 1
        
        
        queue = deque()

        for course in range(n):
            if not indegree[course]:
                queue.append((course, time[course]))
        
        min_months = 0
        temp = [0]*n
        
        while queue:
            
            
            size = len(queue)
            for _ in range(size):
                                
                cur, cur_wait = queue.popleft()
                min_months = max(min_months, cur_wait)
                
                for _next in graph[cur]:
                    indegree[_next] -= 1
                    temp[_next] = max(temp[_next], cur_wait)
                    if not indegree[_next]:
                        queue.append((_next, temp[_next] + time[_next]))
            
        
        return min_months
        
        