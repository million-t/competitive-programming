class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        graph = [[] for node in range(n)]
        indegree = defaultdict(int)
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            indegree[a] += 1
            indegree[b] += 1
        
        queue = deque()
        
        for node in range(n):
            if indegree[node] <= 1:
                queue.append(node)
        
        ans = []
        while queue:
            
            size = len(queue)
            ans = list(queue)
            for _ in range(size):
                cur = queue.popleft()
                
                for neigh in graph[cur]:
                    indegree[neigh] -= 1
                    
                    if indegree[neigh] == 1:
                        queue.append(neigh)
            
        return ans