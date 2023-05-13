class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = [[] for _ in range(numCourses)]
        indegree = defaultdict(int)
        
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        queue = deque()
        
        for course in range(numCourses):
            if not indegree[course]:
                queue.append(course)
        
        order = []
        while queue:
            
            cur = queue.popleft()
            order.append(cur)
            
            for _next in graph[cur]:
                indegree[_next] -= 1
                
                if not indegree[_next]:
                    queue.append(_next)
        
        if len(order) < numCourses:
            order = []
        
        return order