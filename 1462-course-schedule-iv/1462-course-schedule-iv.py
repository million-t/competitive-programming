class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        graph = [[] for _ in range(numCourses)]
        indegree = defaultdict(int)
        
        for a, b in prerequisites:
            graph[a].append(b)
            indegree[b] += 1
        
        queue = deque()
        for course in range(numCourses):
            if not indegree[course]:
                queue.append(course)
        
        prereq_list = [set() for _ in range(numCourses)]
        while queue:
            
            cur = queue.popleft()
            
            for nxt in graph[cur]:
                
                indegree[nxt] -= 1
                prereq_list[nxt].update(prereq_list[cur])
                prereq_list[nxt].add(cur)
                
                if not indegree[nxt]:
                    queue.append(nxt)
                    
        ans = []
        for u, v in queries:
            ans.append(u in prereq_list[v])
        
        return ans