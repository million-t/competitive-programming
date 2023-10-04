class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        
        graph = [[] for _ in range(n)]
        for _from, to, price in flights:
            graph[_from].append((to, price))
            graph[to]
        
        dist = [float('inf')]*n
        heap = [(-1, 0, src)]
        
        while heap:
            moves, dis, node = heappop(heap)
            
            if moves == k + 1 or dis >= dist[node] :
                continue

            dist[node] = dis
            
            for neigh, w in graph[node]:
                heappush(heap, (moves + 1, dis + w, neigh))
        
        return -1 if dist[dst] == float('inf') else dist[dst]