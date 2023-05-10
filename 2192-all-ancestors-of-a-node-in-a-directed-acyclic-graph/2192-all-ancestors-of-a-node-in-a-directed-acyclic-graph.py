class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        graph = [[] for _ in range(n)]
        indegree = defaultdict(int)
        
        
        for _from, to in edges:
            graph[_from].append(to)
            indegree[to] += 1
        
        
        queue = deque()
        for node in range(n):
            if not indegree[node]:
                queue.append(node)
        
        
        ancestors = [ set() for _ in range(n)]
        
        while queue:
            cur = queue.popleft()
            
            for neigh in graph[cur]:
                
                ancestors[neigh] = ancestors[neigh].union(ancestors[cur])
                ancestors[neigh].add(cur)
                
                indegree[neigh] -= 1            
                if not indegree[neigh]:
                    queue.append(neigh)
                    
        
        for index in range(n):
            ancestors[index] = sorted(ancestors[index])   
            
        return ancestors
        
        
        
        
                