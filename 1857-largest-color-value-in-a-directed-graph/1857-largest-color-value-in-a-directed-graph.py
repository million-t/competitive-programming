class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        
        indegree = defaultdict(int)
        graph = [[] for _ in range(len(colors))]
        
        for a, b in edges:
            if a == b:
                return -1
            
            graph[a].append(b)
            indegree[b] += 1
        
        temp = [Counter() for node in range(len(colors))]
        queue = deque()
        
        for node in range(len(colors)):
            if not indegree[node]:
                queue.append(node)
        
        nodes = 0
        ans = 0
        
        while queue:
            cur = queue.popleft()
            temp[cur][colors[cur]] += 1
            ans = max(ans, temp[cur][colors[cur]])
            nodes += 1
            
            for neigh in graph[cur]:
                indegree[neigh] -= 1
                
                for col in temp[cur]:
                    count = temp[cur][col]
                    temp[neigh][col] = max(count, temp[neigh][col])
                    
                if not indegree[neigh]:
                    queue.append(neigh)
                    
        return ans if nodes == len(colors) else -1
                    
            