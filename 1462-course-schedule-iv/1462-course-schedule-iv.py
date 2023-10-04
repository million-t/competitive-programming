class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        
        graph = [[float('inf')]*numCourses for _ in range(numCourses)]
        
        
        for u, v in prerequisites:
            graph[u][v] = 1
        
        
        for k in range(numCourses):
            for row in range(numCourses):
                for col in range(numCourses):
                    graph[row][col] = min(graph[row][col], graph[row][k] + graph[k][col])
        
        
        ans = []
        for u, v in queries:
            # print(graph[row][col])
            if graph[u][v] != float('inf'):
                ans.append(True)
            
            else:
                ans.append(False)
        
        return ans
        