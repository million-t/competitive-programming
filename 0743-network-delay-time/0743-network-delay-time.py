class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        visited = [float('inf')]*(n + 1)
        heap = [(0, k)]
        visited[0] = 0
        
        
        while heap:
            weight, cur = heappop(heap)
            
            if weight >= visited[cur]:
                continue
            
            visited[cur] = weight
            
            for neigh, neigh_weight in graph[cur]:
                heappush(heap, (weight + neigh_weight, neigh))
        
        ans = max(visited)
        return ans if ans != float('inf') else -1
        