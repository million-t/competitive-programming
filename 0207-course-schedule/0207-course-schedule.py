class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        indegree = defaultdict(int)
        graph = [[] for _ in range(numCourses)]
        
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        
        queue = deque()
        
        for course in range(numCourses):
            if not indegree[course]:
                queue.append(course)
        
        count = 0
        while queue:
            cur = queue.popleft()
            count += 1
            
            for neigh in graph[cur]:
                
                indegree[neigh] -= 1
                if not indegree[neigh]:
                    queue.append(neigh)
                
                
        
        return count == numCourses